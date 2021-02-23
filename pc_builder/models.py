from datetime import datetime
from django.db import models
from django.db.models.base import Model
import time

# Create your models here.

class userinfos(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)


class Shopsinfo(models.Model):
    shopename = models.CharField(max_length=32, default=False)
    shopaddress = models.CharField(max_length=500, default=False)
    shopimgaddress = models.CharField(max_length=500,default=False)
    # time = models.DateTimeField(auto_now=False, auto_now_add=True)


class user_cart(models.Model):
    user = models.ForeignKey(userinfos, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shopsinfo,  on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=500,null=True)
    item_link = models.CharField(max_length=500)
    # time = models.DateTimeField(auto_now=False, auto_now_add=True)
    quantity = models.IntegerField(default=1)
    """processors = models.CharField(max_length=500)
    motherboard = models.CharField(max_length=500)
    ram = models.CharField(max_length=500)
    gpu = models.CharField(max_length=500)
    harddisk = models.CharField(max_length=500)
    ssd = models.CharField(max_length=500)
    casing = models.CharField(max_length=500)
    processor_cooler = models.CharField(max_length=500)
"""
class com_details(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    price =  models.CharField(max_length=50)