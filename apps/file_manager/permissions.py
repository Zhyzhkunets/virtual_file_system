from rest_framework.permissions import BasePermission

from apps.file_manager.mixins import PermissionsMixin
from apps.file_manager.models import File
from apps.folder_manager.models import Folder


class FileAccessPermission(PermissionsMixin, BasePermission):
    """
    File permissions
    """

    def has_object_permission(self, request, view, obj):
        public_permissions, personal_permissions, is_owner = self.get_obj_permissions(
            obj, request.user, view.action, File)

        if is_owner or public_permissions.exists() or personal_permissions.exists():
            return True

        return False

    def has_permission(self, request, view):
        if view.action == 'create':
            if not request.data.get('folder'):
                return True

            folder = Folder.objects.filter(id=request.data.get('folder')).first()
            public_permissions, personal_permissions, is_owner = self.get_obj_permissions(
                folder, request.user, view.action, Folder)

            if is_owner or public_permissions.exists() or personal_permissions.exists():
                return True

            return False
        return super().has_permission(request, view)


class FilePermAccessPermission(PermissionsMixin, BasePermission):
    """
    FilePermission permissions
    """

    def has_permission(self, request, view):
        if view.action == 'create':
            if not request.data.get('file'):
                return True

            file = File.objects.filter(id=request.data.get('file')).first()
            if file and file.owner_id != request.user.id:
                return False

        return super().has_permission(request, view)
