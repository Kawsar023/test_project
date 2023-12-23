from django.db import models

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()
    product_qtt = models.IntegerField()
    status = models.BooleanField(default= False)
    
