from django_filters import rest_framework as filters

from apps.file_manager.models import File, FilePermission


class FileFilter(filters.FilterSet):

    class Meta:
        model = File
        fields = ['name', 'folder', 'owner', 'type']


class FilePermissionFilter(filters.FilterSet):

    class Meta:
        model = FilePermission
        fields = ['user', 'permission']
