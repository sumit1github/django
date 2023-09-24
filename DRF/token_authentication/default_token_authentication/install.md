# install
> no installation needed

# settings.py

> INSTALLED_APPS

    AUTH_USER_MODEL = "app_common.User"

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
    }

> Need run migrations and migrate command



# views.py

#### login

    from rest_framework.authtoken.models import Token

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            resp['access_token']= str(token.key)
            resp['status']= 200
            resp['user']= common_serializer.UserSerializer(user).data

#### Logout

    def get(self, request):
        Token.objects.get_or_create(user= request.user).delete()
        return Response({
            "status":200,
            "message":"Logout Successful",
        })