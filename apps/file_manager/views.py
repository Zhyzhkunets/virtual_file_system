from django.contrib.auth.models import Permission
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.file_manager.filters import FileFilter, FilePermissionFilter, PermissionFilter
from apps.file_manager.models import File, FilePermission
from apps.file_manager.permissions import FileAccessPermission
from apps.file_manager.serializers import FileSerializer, FilePermissionSerializer, PermissionSerializer


class FileViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                  mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    File viewset.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated, FileAccessPermission]
    filterset_class = FileFilter
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FileSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
            status.HTTP_404_NOT_FOUND: 'Not found',
        },
        operation_description='Get file by id',
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: FileSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description='Create a new file',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FileSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
            status.HTTP_404_NOT_FOUND: 'Not found',

        },
        operation_description='Update a file',
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FileSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
            status.HTTP_404_NOT_FOUND: 'Not found',
        },
        operation_description='Partial update a file',
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FileSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description="Get list of files"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description="Delete a file"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class FilePermissionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            mixins.CreateModelMixin, mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    File permissions viewset.
    """
    queryset = FilePermission.objects.all()
    serializer_class = FilePermissionSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = FilePermissionFilter

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FilePermissionSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
            status.HTTP_404_NOT_FOUND: 'Not found',
        },
        operation_description='Get file permission by id',
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: FilePermissionSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description='Create a new file permission',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FilePermissionSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
            status.HTTP_404_NOT_FOUND: 'Not found',

        },
        operation_description='Update a file permission',
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FilePermissionSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
            status.HTTP_404_NOT_FOUND: 'Not found',
        },
        operation_description='Partial update a file permission',
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FilePermissionSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description="Get list of file permissions"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description="Delete a file permission"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PermissionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Permissions viewset.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = PermissionFilter

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: PermissionSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_404_NOT_FOUND: 'Not found',
        },
        operation_description='Get permission by id',
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FilePermissionSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description="Get list of permissions"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
