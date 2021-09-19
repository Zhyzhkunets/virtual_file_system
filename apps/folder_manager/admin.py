from django.contrib import admin

from apps.folder_manager.models import Folder, FolderPermission


class FolderPermissionInline(admin.TabularInline):
    model = FolderPermission
    extra = 0


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'owner', 'created_at', 'id')
    search_fields = ('name', 'owner__email', 'owner__username')
    list_filter = ('created_at', 'modified_at')
    readonly_fields = ('modified_at', )
    inlines = [FolderPermissionInline]


@admin.register(FolderPermission)
class FolderPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'folder', 'user', 'permission')
    search_fields = ('user__email', 'user__username', 'permission__codename')
