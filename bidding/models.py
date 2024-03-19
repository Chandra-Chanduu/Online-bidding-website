from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    description=models.TextField()
    minimum_price=models.IntegerField()
    price_interval=models.IntegerField()
    image=models.ImageField(upload_to='uploads/')
    approved=models.BooleanField(default=False,editable=False)