from django.contrib.auth.models import Permission
from django_filters import rest_framework as filters


class PermissionFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')
    codename = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Permission
        fields = ['name', 'content_type', 'codename']
