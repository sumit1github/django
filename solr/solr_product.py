import pysolr
from django.conf import settings
import requests
import json
from .models import Product


def get_all_products():

    queries = '&fq=table:products'

    # Make the Solr API request using the requests library
    url= settings.SOLR_URL + '/select?q.op=OR&q=*:*&rows=10000&wt=json{}'.format(queries)

    search_results= []
    try:
        response = requests.get(url)

        if response.status_code == 200:
            search_results = response.json()['response']['docs']

        else:
            print('Error: failed to get search results from Solr API')

    except Exception as e:
        print(e)
        pass

    return list(search_results)



def solr_product_add_and_update(product):
    try:
        url= settings.SOLR_URL + '/update/?commit=true'
        solr = pysolr.Solr(url)
        if solr.ping():
            print('connection successful')

        product_list = Product.objects.all()

        product_document_list = []

        for product in product_list: 

            product_document ={

            "id": product.solr_product_uid,
            "product_pk": product.id,
            "table":product.table,
            "product_uid": product.uid,

            "name": product.name,
            "manufacturer": product.manufacturer,
            "price": product.price,
            
            "standards": [standard for standard in product.standards],

            'image':[product.image.url  if product.image else None],
            
            }
            product_document_list.append(product_document)

        solr.add(product_document_list)
        solr.commit()
        print("Product Upload is completed")
        return True
    except Exception as e:
        print("Error at Product")
        print(e)
        return False


def product_search(kwargs={}):
    if 'csrfmiddlewaretoken' in kwargs: 
        kwargs.pop('csrfmiddlewaretoken')

    url= settings.SOLR_URL + '/select?q.op=OR&q=*:*&rows=10000&wt=json{}'
     
    search_results= []

    queries = '&q=table:products'

    for key in kwargs:

        if key[0] == "$":
            queries += '&fq={key[1:]}:{kwargs[key[1:]]}'
        else:
            queries += '&fq={}:{}'.format(key,kwargs[key])


    try:
        response = requests.get(url.format(queries))

        if response.status_code == 200:
            search_results = response.json()['response']['docs']

        else:
            print('Error: failed to get search results from Solr API')

        return list(search_results)

    except Exception as e:
        print(e)
        return []
    

def delete_product_from_solr(product):

    try:
        url= settings.SOLR_URL + '/update/?commit=true'
        
        solr = pysolr.Solr(url, timeout=10)
        
        solr.delete(id=str(product.solr_product_uid))

        solr.commit()
        print('Product is deleted from SOLR')
    
    except:
        print('Product is not deleted from SOLR')