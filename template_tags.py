******************* step1*********************
1.create a folder inside app
 mkdir templatetags
2. create file custom_tags.py

*****************step2****************
custom_tags.py
from django import template
from .models import Grievance

register = template.Library()

@register.simple_tag
def new_complaints(dist_object):
    count=Grievance.objects.filter(district=dist_object,status='New').count()
    return count

@register.simple_tag
def new_complaints(dist_object):
    list_data=Grievance.objects.filter(district=dist_object,status='New')
    return list_data
  
 ****************step3**********************
#######template.html

{% extends "starter.html" %}
{%  load static %}
{% load custom_tags %}******************

 <tbody>
{% for dist in district_list %}
    <tr>
    <td><p class="ms-2">#{{dist.code_starting}}{{dist.id}}</p></td>
    <td><p class="ms-2">{{dist.name}}</p></td>
    <td><button type="button"  class="btn_green ms-2">{% new_complaints dist%}</button></td>
    <td><p class="ms-3">{% admin_count dist %}</p></td>
    <td><p class="ms-4">{% subadmin_count dist %}</p></td>
    </tr>
{% endfor %}
