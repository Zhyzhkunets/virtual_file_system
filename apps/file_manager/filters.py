from django_filters import rest_framework as filters

from apps.file_manager.models import File


class FileFilter(filters.FilterSet):

    class Meta:
        model = File
        fields = ['name', 'folder', 'owner', 'type']
