1. pip install -U drf-yasg

2. settings.py

    INSTALLED_APPS = [
       ...
       'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
       'drf_yasg',
       ...
    ]

 3. project.urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Give your title",
        default_version='v1',
        description="service",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
 4.
