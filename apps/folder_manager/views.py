from drf_yasg2.utils import swagger_auto_schema
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated

from apps.folder_manager.filters import FolderFilter
from apps.folder_manager.models import Folder
from apps.folder_manager.serializers import FolderSerializer


class FolderViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                    mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    Folders viewset.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = FolderFilter

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FolderSerializer,
            status.HTTP_404_NOT_FOUND: 'Not found',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description='Get folder by id',
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_201_CREATED: FolderSerializer,
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description='Create a new folder',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FolderSerializer,
            status.HTTP_404_NOT_FOUND: 'Not found',
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description='Update a folder',
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FolderSerializer,
            status.HTTP_404_NOT_FOUND: 'Not found',
            status.HTTP_400_BAD_REQUEST: 'Validation errors',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
        },
        operation_description='Partial update a folder',
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: FolderSerializer,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description="Get list of folders"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={
            status.HTTP_204_NO_CONTENT: None,
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized',
            status.HTTP_403_FORBIDDEN: 'Forbidden',
        },
        operation_description="Delete a folder"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
