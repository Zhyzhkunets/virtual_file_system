from django.contrib.auth.models import Permission
from django.db import models


class Folder(models.Model):
    """
    User folder model
    """
    name = models.CharField(max_length=255)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children',
                               null=True, blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='folders',
                              null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'

    def __str__(self):
        return self.name


class FolderPermission(models.Model):
    """
    Folder permission model
    """

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='permissions',
                               null=True, blank=True)
    user = models.ForeignKey('users.User', related_name='folder_permissions', on_delete=models.SET_NULL,
                             blank=True, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Folder Permission'
        verbose_name_plural = 'Folders Permission'

    def __str__(self):
        return f'{self.permission} | {self.user}'
