from django.contrib.auth.models import Permission
from rest_framework import serializers

from apps.file_manager.models import File, FilePermission


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


class FilePermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilePermission
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'
