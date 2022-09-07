from functools import wraps
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.authtoken.models import Token

from app1_authentication.models import User

def get_user(token):
    user= Token.objects.get(key=token).user
    return (user)

def login_equired_api(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    if "Authorization" not in request.headers:
        res={
            'status':status.HTTP_400_BAD_REQUEST,
            'message':'Authorization Token is Not provided'
        }
        return HttpResponseBadRequest(json.dumps(res), content_type='application/json')

    token = (request.headers.get("Authorization").split(" ")[1])
    request.user=get_user(token)
    
    if request.user:
        
        return function(request, *args, **kwargs)
        
    else:
        data={
            'status':status.HTTP_400_BAD_REQUEST,
            'error':'Login Required!'
        }
    return HttpResponseBadRequest(json.dumps(data), content_type='application/json')

  return wrap


def admin_and_superadmin_api(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    if "Authorization" not in request.headers:
        res={
            'status':status.HTTP_400_BAD_REQUEST,
            'message':'Authorization Token is Not provided'
        }
        return HttpResponseBadRequest(json.dumps(res), content_type='application/json')

    token = (request.headers.get("Authorization").split(" ")[1])
    request.user=get_user(token)
    

    if request.user:
        if request.user.is_admin == True or request.user.is_subadmin == True:
            return function(request, *args, **kwargs)
        else:
            data={
                'status':status.HTTP_400_BAD_REQUEST,
                'error':'Permission Denied!'
            }
            return HttpResponseBadRequest(json.dumps(data), content_type='application/json')
    
    data={
        'status':status.HTTP_400_BAD_REQUEST,
        'error':'Login Required!'
    }
    return HttpResponseBadRequest(json.dumps(data), content_type='application/json')

  return wrap
