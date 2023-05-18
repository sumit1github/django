*************** working with UUID *****************
  import uuid
  
  # generate 5 digit uuid numaric number
  def generate_unique_run_number():
    return str(int(str(uuid.uuid4().int)[:5]))
  
  
  # generate random number
  def generate_unique_orderid():
    return str(uuid.uuid4().int >> 64)
  
  class Order(models.Model):
      order_number= models.CharField(max_length=32, unique=True, blank=True, null=True)
      
  def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = generate_unique_orderid()
        super().save(*args, **kwargs)
        
        
  ***************************** generate a custom media path***************
  
  def rider_document_path(self, filename):
    basefilename, file_extension= os.path.splitext(filename)
    myuuid = uuid.uuid4()
    return 'media/rider_document/{basename}{randomstring}{ext}'.format(basename= basefilename, randomstring= str(myuuid), ext= file_extension)
  
  class RiderProfile(models.Model):
      pan_card_image= models.FileField(upload_to=rider_document_path, null=True, blank=True)

      
 ************************ make all stingfield in lower case (model manager) **********************

# models.py   
class LowercaseManager(models.Manager):
    def create(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, str):
                kwargs[key] = value.lower()
        return super().create(**kwargs)
    
 
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

    objects = LowercaseManager()

    def __str__(self):
        return self.field1
      
 
-------------------------------------------------------- compress Image ----------------------------------
from PIL import Image
import io

class MyModel(models.Model):
image = models.ImageField(upload_to='images/')

def save(self, *args, **kwargs):
    # Open the image file using Pillow
    with Image.open(self.image) as img:
        # Set the maximum size of the image
        max_size = (800, 800)
        # Resize the image while preserving the aspect ratio
        img.thumbnail(max_size, Image.ANTIALIAS)
        # Convert the image to JPEG format
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=75)
        output.seek(0)
        # Save the compressed image to the model field
        self.image = models.ImageFieldFile(output, self.image.name)
    super().save(*args, **kwargs)
    
    
================================================  corvert string to model ================================
from django.apps import apps

# your_app_label = <name of the app, where "Product" model is located>

string_data = "Product"
Product = apps.get_model(app_label='your_app_label', model_name=string_data)
#Product = apps.get_model(app_label='app1_product_master', model_name=string_data)
product_obj2 = Product.objects.all()

================================================  Query Dict to orm query ================================
    model = models.Termination

    def get(self, request): 
        filter_by = request.GET.get("filter_by")
        query = request.GET.get("query")

        termination_list = list(self.model.objects.filter(**{f"{filter_by}__icontains": query}).values())
        
        return JsonResponse(termination_list, safe= False)
