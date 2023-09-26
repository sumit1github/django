# install
>> pip install -U drf-yasg

# settings.py

    INSTALLED_APPS = [
       ...
       'django.contrib.staticfiles',  # required for serving swagger ui's css/js files, if create error revove thia
       'drf_yasg',
       ...
    ]

    SWAGGER_ROOT_URL="https://url.com/swagger/"  <--- production

    SWAGGER_SETTINGS = {
        'USE_SESSION_AUTH': False,
        'JSON_EDITOR': True,
        'api_version': '0.1',
        'enabled_methods': [
            'GET',
            'POST',
        ],
        'SECURITY_DEFINITIONS': {
            "api_key": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            },
        }
    }

# project --> urls.py

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


# swagger fileds

> go to swaggerdoc.md


# views.py 

    from drf_yasg.utils import swagger_auto_schema
    from drf_yasg import openapi
    from . import swagger_doc


#### POST request
    class SignupApi(APIView):

        serializer_class= common_serializer.SignupSerializer
        model= common_model.User
        swagger_doc_item = swagger_doc.sign_up_post

        @swagger_auto_schema(
            tags=swagger_doc_item['tag'],
            operation_id=swagger_doc_item['url_name'],
            operation_description=swagger_doc_item['description'],
            request_body=openapi.Schema(
                
                required=swagger_doc_item['required_fields'],
                type=openapi.TYPE_OBJECT,
                properties = swagger_doc_item['fields'],
            ),
            responses=swagger_doc_item['responses'],
            
        )

#### get request

    class LogOut(APIView):

        swagger_doc_item = swagger_doc.logout_get

        @swagger_auto_schema(
            tags=swagger_doc_item['tag'],
            operation_id=swagger_doc_item['url_name'],
            operation_description=swagger_doc_item['description'],
            responses=swagger_doc_item['responses'],
            
        )


# swagger doc

    from drf_yasg import openapi


#### post request


    sign_up_post = {
        'tag':["Authentication"],
        "url_name": "Sign Up",
        "required_fields" : ['full_name', 'email', 'contact', 'password','confirm_password'],
        "responses" : {201: 'Created', 400: 'Bad Request'},
        "description" : 'Sign Up',

        "fields" : {

            'full_name' : openapi.Schema(type=openapi.TYPE_STRING,max_length=50,description="Full name"),
            
            "email" : openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_EMAIL,description="Email."),

            "contact" : openapi.Schema(type=openapi.TYPE_NUMBER,max_length=15,description="<+country_code><Contact number> "),

            'password' : openapi.Schema(type=openapi.TYPE_STRING,max_length=50,description="Password"),

            'confirm_password' : openapi.Schema(type=openapi.TYPE_STRING,max_length=50,description="Confirm Password"),

            'file' : openapi.Schema(type=openapi.TYPE_FILE,description="mp3 File (SIZE < 25 mb)"),

            'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN,description="Whether the user is active or not."),

            'gender': openapi.Schema(type=openapi.TYPE_STRING,enum=['Male', 'Female', 'Other'],description="Gender",),

            'favorite_colors': openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING),description="List of favorite colors",),

            'birth_date': openapi.Schema(type=openapi.TYPE_STRING,format=openapi.FORMAT_DATE,description="Date of birth (YYYY-MM-DD)",),

            'password': openapi.Schema(type=openapi.TYPE_STRING,format="password",description="Password",),

            'price': openapi.Schema(type=openapi.TYPE_NUMBER,format="float",description="Price as a floating-point number",),
        }
    }

#### get request

> something need to pass in header

    organization_params_in_header = openapi.Parameter(
        "org", openapi.IN_HEADER, required=True, type=openapi.TYPE_INTEGER
    )
        
> get request with header

    account_get_params = [
        organization_params_in_header, # we can remove it if nothing to pass into header
        openapi.Parameter("name", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter("city", openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter("tags", openapi.IN_QUERY, type=openapi.TYPE_STRING),
    ]
