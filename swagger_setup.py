1. pip install -U drf-yasg

2. settings.py

    INSTALLED_APPS = [
       ...
       'django.contrib.staticfiles',  # required for serving swagger ui's css/js files, if create error revove thia
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
       path(
        "swagger/download/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "swagger/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    
 ******************************************************** customization*****************************************
############################ create swagger_data.py in every applications #################################
from drf_yasg import openapi
  
    
# simple post request
post_org_creation_page_params = [

    openapi.Parameter(
        "name", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "address", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "Number of Users", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
    openapi.Parameter(
        "country", openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING
    ),
]

# something need to pass in header
 organization_params_in_header = openapi.Parameter(
    "org", openapi.IN_HEADER, required=True, type=openapi.TYPE_INTEGER
)
    
# get request with header
account_get_params = [
    organization_params_in_header, # we can remove it if nothing to pass into header
    openapi.Parameter("name", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("city", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    openapi.Parameter("tags", openapi.IN_QUERY, type=openapi.TYPE_STRING),
]

############################ views.py ############################
from drf_yasg.utils import swagger_auto_schema
from helper import swagger_params
class ViewName(APIView):
    permission_classes = (IsAuthenticated,)
    
    # both for get and post, same code code need to write 2 times, 1 before get and 2 before post function
    @swagger_auto_schema(
        tags=["auth"],
        operation_description="Your api description",
        manual_parameters=swagger_params.post_org_creation_page_params,
    )
    
 #333333333333333333333333333333 data types list **********************
    TYPE_OBJECT = "object"  #:
TYPE_STRING = "string"  #:
TYPE_NUMBER = "number"  #:
TYPE_INTEGER = "integer"  #:
TYPE_BOOLEAN = "boolean"  #:
TYPE_ARRAY = "array"  #:
TYPE_FILE = "file"  #:

# officially supported by Swagger 2.0 spec
FORMAT_DATE = "date"  #:
FORMAT_DATETIME = "date-time"  #:
FORMAT_PASSWORD = "password"  #:
FORMAT_BINARY = "binary"  #:
FORMAT_BASE64 = "bytes"  #:
FORMAT_FLOAT = "float"  #:
FORMAT_DOUBLE = "double"  #:
FORMAT_INT32 = "int32"  #:
FORMAT_INT64 = "int64"  #:

# defined in JSON-schema
FORMAT_EMAIL = "email"  #:
FORMAT_IPV4 = "ipv4"  #:
FORMAT_IPV6 = "ipv6"  #:
FORMAT_URI = "uri"  #:

# pulled out of my ass
FORMAT_UUID = "uuid"  #:
FORMAT_SLUG = "slug"  #:
FORMAT_DECIMAL = "decimal"

IN_BODY = 'body'  #:
IN_PATH = 'path'  #:
IN_QUERY = 'query'  #:
IN_FORM = 'formData'  #:
IN_HEADER = 'header'  #:

SCHEMA_DEFINITIONS = 'definitions'  #:
