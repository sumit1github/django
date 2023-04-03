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
