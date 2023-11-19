# install
    pip install boto3 django-storages

# settings_prod.py and settings_dev.py

### settings_dev.py
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'staticfiles')
    ]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

### settings_prod.py
    import os
    from dotenv import load_dotenv
    from storages.backends.s3boto3 import S3Boto3Storage

    # Custom storage classes
    class StaticStorage(S3Boto3Storage):
        location = 'staic

    class MediaStorage(S3Boto3Storage):
        location = 'media'
        file_overwrite = False  # Set to True if you want to overwrite files with the same name


    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'
    AWS_DEFAULT_ACL = 'public-read'


    # Static files settings
    STATICFILES_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{STATICFILES_LOCATION}/'
    #STATICFILES_STORAGE = '<django_app_name>.custom_storages.StaticStorage'
    STATICFILES_STORAGE = StaticStorage

    # Media files settings
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{MEDIAFILES_LOCATION}/'
    #DEFAULT_FILE_STORAGE = '<django_app_name>.custom_storages.MediaStorage'
    DEFAULT_FILE_STORAGE = MediaStorage



# settings.py
    import os

    #INSTALLED_APPS
    [
        'storages',
    ]

    if DEBUG:
        from .settings_dev import *
    else:
        from .settings_prod import *

