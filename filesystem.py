------------------------------------------------------- default django filesystem ----------------------------------
from django.core.files.storage import FileSystemStorage
  image = request.FILES['file']
    fs = FileSystemStorage()
    folder_name = f'topalert/{month_num}-{year}' 
    filename = fs.save(f'{folder_name}/{image.name}', image)
    print('media/' +filename)
    
------------------------------------------------------- store data in s3 ----------------------------------
#### To Upload a file

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

s3_file_upload(f"media/topalert/{month_num}-{year}", filename, image)

def s3_file_upload(folder_name ,filename, file_obj):
    import uuid
    import boto3
    from django.conf import settings
    
    filename = str(int(str(uuid.uuid4().int)[:5])) + filename
    s3 = boto3.resource('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
                        
    )
    
    s3_bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
    s3_object = s3_bucket.Object(f"{folder_name}/{filename}")
    s3_object.upload_fileobj(file_obj)
    
    # Return the S3 URL of the uploaded file
    file_path = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{folder_name}/{filename}"
    
    return file_path
  
  
  
  ############# to delte a file 
    filename = str(int(str(uuid.uuid4().int)[:5])) + filename
    s3 = boto3.resource('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,           
    )
    
    s3_bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
    s3_object = s3_bucket.Object(filename)
    response = s3_object.delete()
    return response
