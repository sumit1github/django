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

*****************************************************************************************************************************************************
# let a template tag is returning a list, then how should I render the data


@register.simple_tag
def admin_assigned_to_complaint(complaint):
    count=Grievance.objects.filter(id=complaint.id)
    data=count.filter(assigned_to__is_admin=True).values('assigned_to__first_name')
    final_list=[i.get('assigned_to__first_name') for i in data]
    return (final_list)
   
   
### in html
{% admin_assigned_to_complaint ticket as admin_list%}
  {% for name in admin_list %}
      {{name}}
  {% endfor %}
