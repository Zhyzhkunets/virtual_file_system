from django.contrib.auth import get_user_model
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.serializers import UserSerializer

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    User viewset.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: UserSerializer,
            status.HTTP_404_NOT_FOUND: 'Not found',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description='Get a user',
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: UserSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
        },
        operation_description='Add a new user',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: UserSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description="Get list of users"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
