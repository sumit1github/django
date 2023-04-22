import uuid

def generate_rand_number(digit=5):
    return str(int(str(uuid.uuid4().int)[:digit]))

class Product(models.Model):
    uid = models.CharField(max_length=255, null=True, blank=True)
    solr_product_uid = models.CharField(max_length=255, null=True, blank=True) # for solr
    table=models.CharField(max_length=255, default="product") # for solr purpose
    
    name = models.TextField(null=True, blank=True, unique=True)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default = 0.0)

    image = models.ImageField(upload_to='/products', blank=True, null= True)

    standards = models.JSONField(default=dict, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            rand_uid = generate_rand_number(5)
            self.uid = rand_uid
            self.solr_product_uid = f"products{rand_uid}"
            
        super().save(*args, **kwargs)