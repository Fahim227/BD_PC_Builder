from os import truncate
from django.http import response
from rest_framework import serializers
from pc_builder.models import Shopsinfo, user_cart, userinfos
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pc_builder.serializers import RegisterSerializer
from bs4 import BeautifulSoup
import json
import validators
from urllib import request as rqst
# Create your views here.


@api_view(['POST'])
def home(request):
    comUrl = request.POST.get('comUrl')
    valid = validators.url(comUrl)
    print(valid)
    # brand_name = request.data.get('brandName')
    print(comUrl)
    # if valid==False:
    baseurl = "https://www.startech.com.bd/component/"
    # baseurl+str(component_name).lower()/// baseurl+str(component_name)
    return HttpResponse(scrapcomponents(comUrl))
    
@api_view(['POST'])
def fetchbybrands(request):
    component_name = request.POST.get('brandurl')

    baseurl = "https://www.startech.com.bd/component/"

    return HttpResponse()


def scrapcomponents(baseurl):
    page = rqst.urlopen(baseurl)
    soup = BeautifulSoup(page, "html.parser")
    main_contents = soup.find("div", {"class": "main-content"})
    list_of_home_contents = main_contents.findAll("div", {"class": "p-item"})
    context = []


    for content in list_of_home_contents:
        image = content.find(class_="p-item-img").find("img")
        name = content.find(class_="p-item-name").get_text()
        price = content.find(class_="p-item-price").get_text()
        urls = content.find(class_="p-item-name").find("a")
        con = {
            "images": image['src'],
            "name": name,
            "price": price,
            "urls": urls['href']
        }
        context.append(con)

    context_json = json.dumps(context)
    return context_json


@api_view(['POST'])
def brands(request):
    component_url = request.POST.get('comUrl')
    print(component_url)
    baseurl = "https://www.startech.com.bd/component/casing"
    # baseurl+str(component_name).lower()
    page = rqst.urlopen(component_url)
    soup = BeautifulSoup(page, "html.parser")

    container = soup.find("div", {"class": "child-list"})
    brands = container.findAll('a')
    brand_list = []
    for brand in brands:
        brand_with_link = {
            "name" : brand.get_text(),
            "link" : brand['href']
        }
        brand_list.append(brand_with_link)

    brand_json = {
        "brands": brand_list
    }
    brand_json = json.dumps(brand_json)
    return HttpResponse(brand_json)




@api_view(['POST'])
def brandsAndComponentsName(request):
    """burl = "https://"
    name = request.POST.get('name')
    print(name)
    shopobj = Shopsinfo.objects.get(shopename=name)
    url = shopobj.shopaddress
    print(url)
    url+="/component/"
    burl+=url
    print(burl)"""
    baseurl = "https://www.startech.com.bd/component/"
    # baseurl+str(component_name).lower()
    page = rqst.urlopen(baseurl)
    soup = BeautifulSoup(page, "html.parser")

    container = soup.find("div", {"class": "child-list"})
    brands = container.findAll('a')
    components_list = []
    for brand in brands:
        brand_with_link = {
            "name" : brand.get_text(),
            "link" : brand['href']
        }
        components_list.append(brand_with_link)

    brand_json = {
        "components": components_list
    }
    brand_json = json.dumps(brand_json)
    return HttpResponse(brand_json)



@api_view(['POST'])
def brandscomponents(request):
    casing = "https://www.startech.com.bd/component/casing"
    processor = "https://www.startech.com.bd/component/processor"
    brand_url = request.POST.get('brandurl')
    return HttpResponse(scrapcomponents(brand_url))



@api_view(['POST'])
def register(request):
        serializer = RegisterSerializer(data=request.data)
        responseData = {
            "response" : "Successfully",
             "boolean" : True
        }
        if serializer.is_valid():
            serializer.save()
            return Response(responseData)
        else:
            responseData = {
                "response" : "UnSuccessfully",
                "boolean" : False
            }
            return Response(responseData)
        data ={
                "username" : "Hello",
                "email" : "fahim@gmail.com",
                "password" : "*******"
            }
        return JsonResponse(data)

@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    checking={
        "email" : email,
        "password" : password

    }
    """ return Response(checking)"""

    userauth = userinfos.objects.get(email=email)
    context={}

    if userauth is not None:
        if userauth.password == password:
            context ={
            "user_id" : userauth.id,
            "Auth" : True
            }
        else:
          context ={
             "Auth" : False,
             "real" : userauth.password,
             "given" : password

           }
        
    else:
        context ={
            "Auth" : False
        }
    return Response(context)


"""{
"email" : "fahim@gmail.com",
"password" : "*******"
}"""

@api_view(['POST'])
def componentsdeatils(request):
    gpu = "https://www.startech.com.bd/colorful-geforce-gt710-2gd3-v-graphics-card"
    fan = "https://www.startech.com.bd/corsair-ll120-rgb-dual-light-loop"
    hdd = "https://www.startech.com.bd/toshiba-p300-1tb-internal-hard-drive"
    casing = "https://www.startech.com.bd/xtreme-320-1-casing"
    url = request.POST.get('url')
    print(url)
    jformat = json.dumps(components_in_details(url))
    return HttpResponse(jformat)

def components_in_details(url):
    page = rqst.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    container = soup.find("div", {"class": "col-md-5 left"})
    img_container = container.find("div", {"class": "product-img-holder"})
    img = img_container.find(class_="main-img")['src']
    print(img)
    name = soup.find("div",{"class": "product-short-info"}).find("h1", {"class": "product-name"}).get_text()
    print(name)
    price = soup.find("div", {"class": "product-price-options"}).find(class_="price").get_text()
    ul = soup.find("div",{"class": "full-description"}).find('ul')
    features = []
    desc = ""
    for lis in ul.findAll('li'):
        features.append(lis.get_text()+"\n")
        desc+=lis.get_text()+"\n"
    print(features)
    """description = soup.find("section", {"id": "description"})
    # desc = description.find('p').get_text()
    desc = description.find("div" , {"itemprop": "description"})
    print(desc.get_text())"""

    # print(features)
    # mainjson = []


    con = {
        "img": img,
        "name": name,
        "price": price,
        "description": desc
        # "description": desc.get_text()
    }
    # mainjson.append(con)
    
    return con


@api_view(['POST'])
def add_to_cart(request):
    save_to_cart = user_cart(user_id=request.POST.get('userid'),shop_id=request.POST.get('shopid'),item_link=request.POST.get('produrl'),quantity=request.POST.get('quantity'))
    save_to_cart.save()
    res = {
        'success' : True,
        'message' : "Saved Successfully"
    }
    res_json = json.dumps(res)
    return HttpResponse(res_json)


@api_view(['POST'])
def get_cart_components(request):
    # id = request.POST.get('userID')
    com_obj = user_cart.objects.filter(user_id=request.POST.get('userID'))
    details=[]
    for com in com_obj:
        con = components_in_details(com.item_link)
        details.append(con)
    
    jshow = json.dumps(details)
    return HttpResponse(jshow)


@api_view(['GET'])
def allshopsAPI(request):
    shops = Shopsinfo.objects.all()
    context = []
    for shop in shops:
        shopdetails = {
            "shop_name" : shop.shopename,
            "shop_address" : shop.shopaddress,
            "shop_img" : shop.shopimgaddress,
            "shop_id" : shop.id
        }
        context.append(shopdetails)
    shops_json = json.dumps(context)
    return HttpResponse(shops_json)