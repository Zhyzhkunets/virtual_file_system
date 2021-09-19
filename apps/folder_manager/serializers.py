from rest_framework import serializers

from apps.folder_manager.models import Folder, FolderPermission


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'


class FolderPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = FolderPermission
        fields = '__all__'
