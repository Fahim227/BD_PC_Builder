
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('getproducts/', views.home, name='home'),
    path('getComponentsAndBrandsName/', views.brandsAndComponentsName, name='getComponentsAndBrandsName'),
    path('getbrands/', views.brands, name='getbrands'),
    path('componentdetails/', views.componentsdeatils, name='componentdetails'),
    path('brandscomponents/', views.brandscomponents, name='brandscomponents'),  

]
