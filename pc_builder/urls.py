
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('getproducts/', views.home, name='home'),
    path('getbrands/', views.brands, name='getbrands'),
    path('/register/', views.register, name='register'),
    path('/login/', views.login, name='login'),
    path('componentdetails/', views.componentsdeatils, name='componentdetails'),
    path('brandscomponents/', views.brandscomponents, name='brandscomponents'),
    path('addtocart/', views.add_to_cart, name='addtocart'),
    path('get_cart_components/', views.get_cart_components, name='get_cart_components'),
    path('insertshop/',views.insertshop, name='addshop'),
    path('allshops/',views.allshops, name='allshops'),
    path('editshop/<int:shopid>',views.editshop, name='editshop'),
    path('deleteshop/<int:shopid>',views.deleteshop, name='deleteshop'),
     path('allshopsapi/',views.allshopsAPI, name='allshopsapi'),

]
