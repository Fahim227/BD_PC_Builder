from datetime import datetime
from django.db import models
from django.db.models.base import Model
import time
import datetime
# Create your models here.

class userinfos(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)


class Shopsinfo(models.Model):
    shopname = models.CharField(max_length=32, default=False)
    shopaddress = models.CharField(max_length=500, default=False)
    shopimgaddress = models.CharField(max_length=500,default=False)


class user_cart(models.Model):
    user = models.ForeignKey(userinfos, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shopsinfo,  on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=500,null=True)
    item_link = models.CharField(max_length=500)
    quantity = models.IntegerField(default=1)
    added_time = models.DateTimeField(auto_now_add=True)

class com_details(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    price =  models.CharField(max_length=50)