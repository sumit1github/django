------------------------------------------------------- default django filesystem ----------------------------------
from django.core.files.storage import FileSystemStorage
  image = request.FILES['file']
    fs = FileSystemStorage()
    folder_name = f'topalert/{month_num}-{year}' 
    filename = fs.save(f'{folder_name}/{image.name}', image)
    file_url = fs.url(filename)
    file_path = fs.path(filename)
    
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
  
  
  ------------------------------------------------------- store data in s3 and compress ----------------------------------
import uuid
import boto3
from django.conf import settings
from PIL import Image
import io

s3 = boto3.resource('s3')

def s3_file_upload(folder_name, filename, file_obj):
    # Generate a unique filename
    filename = str(int(str(uuid.uuid4().int)[:5])) + filename

    # Upload the original file to S3
    s3_bucket = s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME)
    s3_object = s3_bucket.Object(f"{folder_name}/{filename}")
    s3_object.upload_fileobj(file_obj)

    # Compress the image if it is an image file
    if 'image' in file_obj.content_type:
        # Open the image file using Pillow
        with Image.open(file_obj) as img:
            # Set the maximum size of the image
            max_size = (800, 800)
            # Resize the image while preserving the aspect ratio
            img.thumbnail(max_size, Image.ANTIALIAS)
            # Convert the image to JPEG format
            output = io.BytesIO()
            img.save(output, format='JPEG', quality=75)
            output.seek(0)
            # Upload the compressed image to S3
            s3_compressed_object = s3_bucket.Object(f"{folder_name}/compressed/{filename}")
            s3_compressed_object.put(Body=output.getvalue(), ContentType='image/jpeg')
            # Return the S3 URL of the compressed image
            file_path = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{folder_name}/compressed/{filename}"
    else:
        # Return the S3 URL of the original file
        file_path = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{folder_name}/{filename}"

    return file_path
