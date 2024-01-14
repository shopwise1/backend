from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Vendor Model
class Vendor(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

