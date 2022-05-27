from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from re_path
Install drf_yasg

pip install drf_yasg

Add this in settings.py installed apps after django.config.staticfiles

'drf_yasg',

Add schema and urls in urls

Import this lines


Add this above url patterns

schema_view = get_schema_view(
    openapi.Info(title="ESG APIs", default_version="v1",
                 description="ESG APIs"),
    public=True,
    permission_classes=[permissions.AllowAny],
)


In url patterns add this

re_path(
    r"^swagger(?P<format>\.json|\.yaml)$",
    schema_view.without_ui(cache_timeout=0),
    name="schema-json",
),
re_path(
    r"^swagger/$",
    schema_view.with_ui("swagger", cache_timeout=0),
    name="schema-swagger-ui",
),
re_path(
    r"^redoc/$",
    schema_view.with_ui("redoc", cache_timeout=0),
    name="schema-redoc",
),


For Custom parameters and body add in views


GET METHOD - PARAMS

lesson_id = openapi.Parameter(
    "lesson_id", openapi.IN_QUERY, description="Lesson Id", type="id"
)


@swagger_auto_schema(
    method="get",
    manual_parameters=[lesson_id],
)
POST METHOD - BODY


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "status": openapi.Schema(type="string", description="status"),
            "is_video": openapi.Schema(type="string", description="true or false"),
        },
    ),
)
