from django import forms
from helpers import utils
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.forms.utils import ValidationError


class MaxFileSizeValidator:
    def __init__(self, max_size=20*1024):
        self.max_size = max_size

    def __call__(self, file):
        if file.size > self.max_size:
            raise ValidationError(f"For performence purpose file-size should not exceed {self.max_size/1024} KB.")

            
            
            
            
            
    image = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg','png']),  MaxFileSizeValidator(20*1024)]
    ) # 20 = kb
