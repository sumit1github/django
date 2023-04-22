from django.core.management.base import BaseCommand
import pysolr
from django.conf import settings


def populate_product():
    from .models import Product
    try:
        url= settings.SOLR_URL + '/update/?commit=true'
        solr = pysolr.Solr(url)
        if solr.ping():
            print('connection successful for Products')


        product_list = Product.objects.all()

        product_document_list = []

        for product in product_document_list: 

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
        print("product Upload is completed")
        return True
    except Exception as e:
        print("Error at product")
        print(e)
        return False
    


class Command(BaseCommand):
    help = 'Populate solr Database'

    def handle(self, *args, **kwargs):
        populate_product()
        print('All Process completed')