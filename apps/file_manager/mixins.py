from django.contrib.contenttypes.models import ContentType


class PermissionsMixin:
    """
    Mixin for view permissions
    """

    actions = {
        'retrieve': 'view_file',
        'list': 'view_file',
        'create': 'add_file',
        'destroy': 'delete_file',
        'partial_update': 'change_file',
        'update': 'change_file'
    }

    def get_obj_permissions(self, obj, user, view_action, model):
        queryset = obj.permissions.filter(permission__codename=self.actions[view_action],
                                          permission__content_type=ContentType.objects.get_for_model(model))
        public_permissions = queryset.filter(user__isnull=True)
        personal_permissions = queryset.filter(user_id=user.id)
        is_owner = obj.owner.id == user.id if obj.owner else False

        return public_permissions, personal_permissions, is_owner
