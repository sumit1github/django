# install
>> pip install djangorestframework-simplejwt

# settings.py

> INSTALLED_APPS

    INSTALLED_APPS = [
        "rest_framework_simplejwt",
        "rest_framework_simplejwt.token_blacklist",
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
        "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
        "ROTATE_REFRESH_TOKENS": True,
        "BLACKLIST_AFTER_ROTATION": True,
        "UPDATE_LAST_LOGIN": True,

        "ALGORITHM": "HS256",
        "SIGNING_KEY": SECRET_KEY,
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
        "SLIDING_TOKEN_LIFETIME": timedelta(days=7),
        "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),

        "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
        "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
        "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
        "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
        "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
        "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
    }

# views.py

    from rest_framework.views import APIView
    from django.contrib.auth import authenticate
    from rest_framework.response import Response

    from rest_framework_simplejwt.tokens import RefreshToken
    from rest_framework_simplejwt.views import TokenRefreshView

> Login API

    class Login(APIView):

        model= models.User
        serializer_class = serializers.LoginSerializer

        def post(self, request):
            resp ={}
            serilizer = self.serializer_class(data = request.data)

            if serilizer.is_valid():
                uid = request.data.get('uid')
                password =request.data.get('password')

                user = auth.authenticate(username=uid, password=password)
                if user:

                    access_token, refresh_token = self.get_tokens_for_user(user)
                
                    resp['access_token']= access_token
                    resp['refresh_token'] = refresh_token
                    resp['status']= 200
                else:
                    resp['status']= 400
                    resp['message']= ""


            resp['status']= 400
            resp['message']= ""
            return Response(resp)
        

        def get_tokens_for_user(self, user):
            refresh = RefreshToken.for_user(user)

            return (str(refresh.access_token), str(refresh))


> refresh Token

* need to send refresh token inside body > key: refresh, value: refresh_token

    class RefreshTokenView(TokenRefreshView):

        swagger_doc_item = swagger_doc.refresh_token_post

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

        def post(self, request, *args, **kwargs):
            # Add your custom logic here.
            return super().post(request, *args, **kwargs)

> Logout api

    class LogoutApi(APIView):

        permission_classes = ([IsAuthenticated,])

        def post(self, request):
            refresh = RefreshToken.for_user(request.user)
            return Response({
                "status":200,
                "message":"Logout Done..",
            })