class BaseModel(models.Model):
    org_name=models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        abstract = True
 

class BaseModel2(models.Model):
    kaka=models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        abstract = True
 

class MainModel(BaseModel,BaseModel2):
    text_data=models.CharField(max_length=255, null=True, blank=True)
    
note***:
  after maigrate only main model will be created and 
  org_name and kaka attributes will be inside the model.
  
 
usercase: 
  if there are some repetative attibutes in every model like, eg: created_date, is_active
    in that case we can use it.
