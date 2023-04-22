from django import template
register = template.Library()
from django.conf import settings
import requests
import json

from ..solr_product import get_all_products


@register.simple_tag
def more_filter_options():

    product_list= get_all_products()

    manufacturer=[]


    for product in product_list:
        

        try:
            if (product['manufacturer']) and (product['manufacturer'] not in manufacturer):
                manufacturer.append(product['manufacturer'])
        except:
            pass



    return {
        "manufacturer":manufacturer
    }

@register.simple_tag
def menu_data_list(data_dict,menu_name):
    return data_dict[menu_name]

@register.filter
def text_filter(text):
    try:
        return text[0]
    except:
        return None
