from django.core.management.base import BaseCommand
import pysolr
from django.conf import settings

class Command(BaseCommand):
    help = 'Delete Solr Records'

    def handle(self, *args, **kwargs):
        url= settings.SOLR_URL + '/update/?commit=true'
        
        solr = pysolr.Solr(url, timeout=10)
        id_list = ['solr_product_uid1','solr_product_uid2']
        for id in id_list:
            solr.delete(id=str(id))

        solr.commit()
        print('Delete Process is completed..')