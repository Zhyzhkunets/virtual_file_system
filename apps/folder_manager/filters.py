from django_filters import rest_framework as filters

from apps.folder_manager.models import Folder


class FolderFilter(filters.FilterSet):

    class Meta:
        model = Folder
        fields = ['name', 'parent', 'owner']
