how to user two authentication table in django


class User1(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class User2(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    
# create a file: custom_backend.py in same dir of models.py
from django.contrib.auth.backends import BaseBackend

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user1 = User1.objects.get(username=username, password=password)
        except User1.DoesNotExist:
            try:
                user2 = User2.objects.get(username=username, password=password)
            except User2.DoesNotExist:
                return None

        if user1:
            return user1
        else:
            return user2

    def get_user(self, user_id):
        try:
            return User1.objects.get(pk=user_id)
        except User1.DoesNotExist:
            try:
                return User2.objects.get(pk=user_id)
            except User2.DoesNotExist:
                return None
    
   ### add in seetings.py
  AUTHENTICATION_BACKENDS = [    'path.to.CustomAuthBackend',]

