from rest_framework.permissions import BasePermission

from apps.file_manager.mixins import PermissionsMixin
from apps.folder_manager.models import Folder


class FolderPermission(PermissionsMixin, BasePermission):
    """
    Check folder permissions
    """

    def has_object_permission(self, request, view, obj):
        public_permissions, personal_permissions, is_owner = self.get_obj_permissions(
            obj, request.user, view.action, Folder)

        if is_owner or public_permissions.exists() or personal_permissions.exists():
            return True

        return False

    def has_permission(self, request, view):
        if view.action == 'create':
            if not request.data.get('parent'):
                return True

            folder_parent = Folder.objects.filter(id=request.data.get('parent')).first()
            public_permissions, personal_permissions, is_owner = self.get_obj_permissions(
                folder_parent, request.user, view.action, Folder)

            if is_owner or public_permissions.exists() or personal_permissions.exists():
                return True

        return False
