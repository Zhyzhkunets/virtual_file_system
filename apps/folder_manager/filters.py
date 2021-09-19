from django_filters import rest_framework as filters

from apps.folder_manager.models import Folder, FolderPermission


class FolderFilter(filters.FilterSet):

    class Meta:
        model = Folder
        fields = ['name', 'parent', 'owner']


class FolderPermissionFilter(filters.FilterSet):

    class Meta:
        model = FolderPermission
        fields = ['folder', 'user', 'permission']
