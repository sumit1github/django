# usecase
if in models.py email is the username field and we want to use the authenticate function inside views.py with some diffrent field(eg : uid).

Just trying to override the authenticate function

# models.py


    USERNAME_FIELD = "email"	
    REQUIRED_FIELDS = ["password"]

    objects = MyAccountManager()

# views.py
    from django.contrib.auth import authenticate


    class Login:
        user = authenticate(username=uid, password=password)

# auth_backend.py

> dir -> inside common app

> it will support both the email and uid

    from django.contrib.auth import backends
    from .models import User

    class UIDPasswordAuthenticationBackend(backends.BaseBackend):
        """
        Authentication backend that allows users to log in using their UID and password.
        """

        def authenticate(self, request, username=None, password=None, **kwargs):
            UserModel = User

            try : 
                if "@" in username:
                    user = UserModel.objects.get(email=username)
                else:
                    user = UserModel.objects.get(uid=username)
            except:
                return None


            if user.check_password(password):
                return user
            else:
                return None

# settings.py

    AUTHENTICATION_BACKENDS = [
        "common.auth_backend.UIDPasswordAuthenticationBackend",
        "django.contrib.auth.backends.ModelBackend",
    ]

` "common.auth_backend.UIDPasswordAuthenticationBackend",` need to add at first.