from django.db import models
from django.db.models.base import Model

# Create your models here.

class userinfos(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)


class Shopsinfo(models.Model):
    shopename = models.CharField(max_length=32)
    shopaddress = models.CharField(max_length=500)
    processors = models.CharField(max_length=500)
    motherboard = models.CharField(max_length=500)
    ram = models.CharField(max_length=500)
    gpu = models.CharField(max_length=500)
    harddisk = models.CharField(max_length=500)
    ssd = models.CharField(max_length=500)
    casing = models.CharField(max_length=500)
    processor_cooler = models.CharField(max_length=500)


class user_cart(models.Model):
    user_id = models.ForeignKey(userinfos, on_delete=models.CASCADE)
    shop_id = models.ForeignKey(Shopsinfo,  on_delete=models.CASCADE)
    shop = models.CharField(max_length=500)
    processors = models.CharField(max_length=500)
    motherboard = models.CharField(max_length=500)
    ram = models.CharField(max_length=500)
    gpu = models.CharField(max_length=500)
    harddisk = models.CharField(max_length=500)
    ssd = models.CharField(max_length=500)
    casing = models.CharField(max_length=500)
    processor_cooler = models.CharField(max_length=500)
