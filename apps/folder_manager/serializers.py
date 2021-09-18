from rest_framework import serializers

from apps.folder_manager.models import Folder


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'


