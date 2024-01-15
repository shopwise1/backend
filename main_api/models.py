from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Vendor Model
class Vendor(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

#Products Category
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title
    
#Products
class Product(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title