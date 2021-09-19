from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from apps.file_manager.models import File
from apps.file_manager.serializers import FileSerializer

User = get_user_model()


class FileModelTest(TestCase):
    """
    File module tests
    """

    def setUp(self):
        File.objects.create(name='Test 1', text='Test desc 1')
        File.objects.create(name='Test 2', text='Test desc 2')

    def test_file_text(self):
        file_test_1 = File.objects.get(name='Test 1')
        file_test_2 = File.objects.get(name='Test 2')
        self.assertEqual(file_test_1.text, 'Test desc 1')
        self.assertEqual(file_test_2.text, 'Test desc 2')


class FileAPITest(TestCase):
    """
    File API tests
    """

    def setUp(self):
        user = User.objects.create(email='test_user@mail.com', username='test_user')
        user.set_password('1234qwer')
        user.save(update_fields=['password'])
        self.user = user

        File.objects.create(name='Test1', text='Test desc 1')
        File.objects.create(name='Test2', text='Test desc 2', owner=user)

    def test_get_all_files_not_auth(self):
        response = self.client.get(reverse('file-list'))
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_all_files_auth(self):
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'email': 'test_user@mail.com', 'password': '1234qwer'},
                                    format='json')
        self.assertIn('access', response.data)

        response = self.client.get(reverse('file-list'), {}, HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)

        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_auth(self):
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'email': 'test_user@mail.com', 'password': '1234qwer'},
                                    format='json')
        self.assertIn('access', response.data)

        file_id = File.objects.filter(owner=self.user).first().id
        response = self.client.get(reverse('file-detail', args=(file_id, )), {},
                                   HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")
        file = File.objects.get(id=file_id)
        serializer = FileSerializer(file)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_file_auth_not_owner(self):
        response = self.client.post(reverse('token_obtain_pair'),
                                    {'email': 'test_user@mail.com', 'password': '1234qwer'},
                                    format='json')
        self.assertIn('access', response.data)

        file_id = File.objects.first().id
        response = self.client.get(reverse('file-detail', args=(file_id, )), {},
                                   HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

        self.assertEqual(response.data['detail'], 'You do not have permission to perform this action.')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# TODO: write more test next time :)
