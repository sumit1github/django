
# model manager
IF want a enable a code or logic for all models, For this we can use model manager.

eg : I want to a custom query enable for models


# ------------------------- manger.py -----------------------
class CommonQueryManager(models.Manager):
    def get_object(self, **kwargs):
        try: 
            obj = self.get(**kwargs)
            return (True, obj)
        
        except Exception as e:
            return (False, str(e))


# ---------------------- models.py ----------------------------
from .manager import CommonQueryManager
class Expence(models.Model):
    title = models.CharField(max_length=255, null= True)
    description = models.TextField(blank=True, null= True)
    amount = models.FloatField(default=0.0)
    date = models.DateField(null= True, blank= True)

    ` here we are importing `
    objects = some_other_manager()
    query_objects = CommonQueryManager()  #here we are adding our manager

