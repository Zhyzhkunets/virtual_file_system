from django.contrib.auth.models import Permission
from django.db import models

from apps.folder_manager.models import Folder


class File(models.Model):
    """
    User file model
    """
    FILE_TYPE_TEXT = 'text'
    FILE_TYPE_FILE = 'file'
    FILE_TYPE_LIST = (
        (FILE_TYPE_TEXT, 'Text'),
        (FILE_TYPE_FILE, 'File'),
    )

    name = models.CharField(max_length=255)
    text = models.TextField(max_length=1000, blank=True)

    type = models.CharField(max_length=15, choices=FILE_TYPE_LIST, default=FILE_TYPE_TEXT)
    file = models.FileField(max_length=255, upload_to='files', blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL, related_name='files',
                               null=True, blank=True)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='files',
                              null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.name


class FilePermission(models.Model):
    """
    File permission model
    """

    name = models.CharField(max_length=255)

    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='permissions', null=True, blank=True)
    user = models.ForeignKey('users.User', related_name='file_permissions', on_delete=models.SET_NULL,
                             blank=True, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'File Permission'
        verbose_name_plural = 'Files Permission'

    def __str__(self):
        return self.name
