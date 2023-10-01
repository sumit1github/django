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
    from .swagger_doc import get_swagger_api_details


#### POST request
    class SignupApi(APIView):

        serializer_class= common_serializer.SignupSerializer
        model= common_model.User

        @swagger_auto_schema(**get_swagger_api_details("create_meeting_id_post"))

#### get request

    class LogOut(APIView):
        
        from .swagger_doc import get_swagger_api_details

        @swagger_auto_schema(**get_swagger_api_details("create_meeting_id_post"))
        def get():
        pass



# swagger doc

    from drf_yasg import openapi


    
    api_details = {
        "signup_post" : {
            "tags": ["StandAlone - Meeting",],
            "operation_id": "Create Meeting ID",
            "operation_description": 'Creating meeting id when we are scheduling a meeting...',
            "request_body": openapi.Schema(
                required=['uid',],
                type=openapi.TYPE_OBJECT,
                properties={
                    "uid" : openapi.Schema(type=openapi.TYPE_STRING,description="uid."),
                    'name' : openapi.Schema(type=openapi.TYPE_STRING,max_length=50,description="Meeting Title"),
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
            ),
            "responses": {201: 'Success', 400: 'Bad Request',},
        },

        "meeting_details_get":{
            "tags": ["StandAlone - Meeting",],
            "operation_id": "Meeting Details",
            "operation_description": 'There is no function is acssociated with it',
            "responses": {200: 'Success', 400: 'Bad Request',},
            "manual_parameters":[
                openapi.Parameter("meeting_id", openapi.IN_QUERY,required=True, type=openapi.TYPE_STRING),
            ]
        }, 
    }
        


    def get_swagger_api_details(function_name):
        return api_details[function_name]
