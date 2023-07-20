

******* settings.py*********

INSTALLED_APPS = [
	'celery',
]


CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


*********************************************************
go to project folder where settings.py

******************** celery.py ***********
import os

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
app = Celery('project_name')
CELERY_CONFIG = {
    'broker_connection_retry_on_startup': True,
}

# Updating the Celery configuration with the new settings
app.conf.update(**CELERY_CONFIG)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
*************************** __init__.py*******************************
from .celery import app as celery_app
__all__ = ('celery_app',)


*************************** views.py********************
send_mail.delay(email_id)


************************* tasks.py ***********************


from celery import shared_task
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import get_template
from .models import Order
from app_common.checkout.serializer import OrderSerializer

@shared_task
def send_forgot_password_link(user_id ,email, otp):
    html_tpl_path = 'app_common/authentication/forgot_password_email_template.html'

    encoded_user_id= urlsafe_base64_encode(str(user_id).encode('utf-8'))


    url=settings.DOMAIN_NAME+'new_password_set/{}/{}'.format(encoded_user_id, otp)

    context={
        "reciver_email":email,
        "url": url
    }
    email_html_template = get_template(html_tpl_path).render(context)

    subject = 'Forgot Password - LakshmiMart'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    email_msg=EmailMessage( subject, email_html_template, email_from, recipient_list )
    email_msg.content_subtype = 'html'

    
    try:
        email_msg.send(fail_silently=False)
    except Exception as e:
        print("#############################################")
        print(str(e))
        print("#############################################")




@shared_task
def share_invoice(email,data):

    html_tpl_path = 'app_common/checkout/invoice.html'


    for product in data['products']:
        product['product']['quantity']=product['quantity']

    context ={
        'order':data,
        'address':data['address'],
        'product_list':data['products'],
        'charges':data['order_meta_data']['charges'],
        'gross_amt':data['order_meta_data']['our_price'],
        'discount':data['order_meta_data']['our_price'] - data['order_value'],
    }
    email_html_template = get_template(html_tpl_path).render(context)

    subject = 'Invoice - LakshmiMart'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, 'lakshmimart.tapas@gmail.com',]
    email_msg=EmailMessage( subject, email_html_template, email_from, recipient_list )
    email_msg.content_subtype = 'html'

    
    try:
        email_msg.send(fail_silently=False)
    except Exception as e:
        print("#############################################")
        print(str(e))
        print("#############################################")














