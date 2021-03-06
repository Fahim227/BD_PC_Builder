
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('getproducts/', views.home, name='home'),
    path('getComponentsAndBrandsName/', views.brandsAndComponentsName, name='getComponentsAndBrandsName'),
    path('/register/', views.register, name='register'),
    path('/login/', views.login, name='login'),
    path('getbrands/', views.brands, name='getbrands'),
    path('componentdetails/', views.componentsdeatils, name='componentdetails'),
    path('brandscomponents/', views.brandscomponents, name='brandscomponents'),
    path('addtocart/', views.add_to_cart, name='addtocart')

]
