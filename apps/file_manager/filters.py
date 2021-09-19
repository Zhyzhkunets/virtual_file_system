from django.contrib.auth.models import Permission
from django_filters import rest_framework as filters

from apps.file_manager.models import File, FilePermission


class FileFilter(filters.FilterSet):

    class Meta:
        model = File
        fields = ['name', 'folder', 'owner', 'type']


class FilePermissionFilter(filters.FilterSet):

    class Meta:
        model = FilePermission
        fields = ['name', 'file', 'user', 'permission']


class PermissionFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')
    codename = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Permission
        fields = ['name', 'content_type', 'codename']
