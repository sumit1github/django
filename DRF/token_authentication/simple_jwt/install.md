# install
>> pip install djangorestframework-simplejwt

# settings.py

> INSTALLED_APPS

    INSTALLED_APPS = [
        "rest_framework_simplejwt",

        #my apps
        "common",
    ]


    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    }

> Need run migrations and migrate command

>> from datetime import timedelta

> JWT Settings

    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
        "ROTATE_REFRESH_TOKENS": False,
        "BLACKLIST_AFTER_ROTATION": False,
        "UPDATE_LAST_LOGIN": False,

        "ALGORITHM": "HS256",
        "SIGNING_KEY": settings.SECRET_KEY,
        "VERIFYING_KEY": "",
        "AUDIENCE": None,
        "ISSUER": None,
        "JSON_ENCODER": None,
        "JWK_URL": None,
        "LEEWAY": 0,

        "AUTH_HEADER_TYPES": ("token",),
        "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
        "USER_ID_FIELD": "id",
        "USER_ID_CLAIM": "user_id",
        "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

        "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
        "TOKEN_TYPE_CLAIM": "token_type",
        "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

        "JTI_CLAIM": "jti",

        "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
        "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
        "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

        "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
        "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
        "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
        "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
        "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
        "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
    }


# views.py

    from rest_framework.views import APIView
    from rest_framework_simplejwt.tokens import RefreshToken
    from django.contrib.auth import authenticate
    from rest_framework.response import Response
    from rest_framework.permissions import IsAuthenticated

> Login API

    class LoginView(APIView):
        permission_classes = ([IsAuthenticated,])
        
        def post(self, request):
            if not request.data.get('email') or not request.data.get('password'):

                return Response({
                    'status': 400,
                    'error': [
                        'email and password is needed..',
                    ],
                })
            
            print(request.data.get('email'), request.data.get('password'))s
            user = authenticate(
                request,
                email= request.data.get('email'), 
                password= request.data.get('password'),
            )
            print(user)
            if user is not None:
                refresh = RefreshToken.for_user(user)

                return Response({
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                })
            
            else:
                return Response({
                    "status":400,
                    "error":[
                        "Login failed ....",
                    ]
                })

> Logout api

    class LogoutApi(APIView):

        permission_classes = ([IsAuthenticated,])

        def post(self, request):
            refresh = RefreshToken.for_user(request.user)
            return Response({
                "status":200,
                "message":"Logout Done..",
            })