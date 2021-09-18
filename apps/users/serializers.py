from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser', 'groups', 'user_permissions']
        read_only_fields = ('is_active', 'last_login', 'date_joined')
