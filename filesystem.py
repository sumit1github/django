------------------------------------------------------- default django filesystem ----------------------------------
from django.core.files.storage import FileSystemStorage
  image = request.FILES['file']
    fs = FileSystemStorage()
    folder_name = f'topalert/{month_num}-{year}' 
    filename = fs.save(f'{folder_name}/{image.name}', image)
    print('media/' +filename)
    
------------------------------------------------------- store data in s3 ----------------------------------
pip install boto3
# settings.py

AWS_ACCESS_KEY_ID = 'your_access_key'
AWS_SECRET_ACCESS_KEY = 'your_secret_key'
AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
AWS_S3_REGION_NAME = 'your_bucket_region'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# views
import boto3
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


myfile = request.FILES['file']

# Generate a unique filename for the file
filename = myfile.name
s3 = boto3.resource('s3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name=settings.AWS_S3_REGION_NAME,
                    endpoint_url=settings.AWS_S3_ENDPOINT_URL)
s3_bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
s3_object = s3_bucket.Object(filename)
s3_object.upload_fileobj(myfile)

# Return a JSON response with the S3 URL of the uploaded file
file_url = f"{settings.AWS_S3_CUSTOM_DOMAIN}/{filename}"
