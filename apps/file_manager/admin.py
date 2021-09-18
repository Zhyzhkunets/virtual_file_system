from django.contrib import admin

from apps.file_manager.models import File, FilePermission


class FilePermissionInline(admin.TabularInline):
    model = FilePermission
    extra = 0


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'folder', 'owner', 'created_at', 'id')
    search_fields = ('name', 'owner__email', 'owner__username')
    list_filter = ('type', 'created_at', 'modified_at')
    readonly_fields = ('modified_at', )
    inlines = [FilePermissionInline]


@admin.register(FilePermission)
class FolderPermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'user', 'permission', 'id')
    search_fields = ('name', 'user__email', 'user__username')
