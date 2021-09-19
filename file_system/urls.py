"""file_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions, routers
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.file_manager.views import FileViewSet, FilePermissionViewSet, PermissionViewSet
from apps.folder_manager.views import FolderViewSet
from apps.users.views import UserViewSet

schema_view = get_schema_view(
  openapi.Info(
     title='FS API',
     default_version='v1',
     description='FS description',
  ),
  public=settings.DEBUG,
  permission_classes=(permissions.AllowAny if settings.DEBUG else permissions.IsAuthenticated,),
)

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'folders', FolderViewSet)
router.register(r'files', FileViewSet)
router.register(r'files-permission', FilePermissionViewSet)
router.register(r'permission', PermissionViewSet)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
