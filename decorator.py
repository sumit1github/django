from functools import wraps
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.authtoken.models import Token

from app1_authentication.models import User


------------------------------------------------------ decorator with arguments ---------------------------------------
## we can pass arguments to this decorator

def has_permission(permission_name):
  def _method_wrapper(function):
    def _arguments_wrapper(request, *args, **kwargs):
      if permission_name not in access_list :
        return HttpResponse('Enter An valid access name.')
      user=request.user
      if user.is_superuser or user.is_org_admin or permission_name in user.access:
        return function(request, *args, **kwargs)
      else:
        return HttpResponse('Permission denied!!' )
    return _arguments_wrapper
  return _method_wrapper
############################ use ##########################
from django.utils.decorators import method_decorator


@method_decorator(has_permission('contact(this is the augument)'),name='dispatch')
###########################################################
-----------------------------------------------------------------------------------------------------------------------


------------------------------------------------- decorator in rest freamework ----------------------------------------
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
-----------------------------------------------------------------------------------------------------------------------
