****************** models.py***********************
class Category(models.Model):
  name=models.CharField()
 
class Product(models.Model):
  cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
  name=models.CharField()

**************************************views.py***********************************
category_list=Category.objects.all()
CategoryListSerializer(category_list,many=True).data
************************************** category serializer *******************************

class CategoryListSerializer(serializers.ModelSerializer):
    product_list = serializers.SerializerMethodField()

    def get_product_list(self, obj):
        product=Product.objects.filter(cat=obj.id)
        return product.values_list('name', flat=True)
    class Meta:
        model = Category
        fields = ['name','product_list']
