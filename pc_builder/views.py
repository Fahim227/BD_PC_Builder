from django.http import response
from rest_framework import serializers
from pc_builder.models import userinfos
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer
from bs4 import BeautifulSoup
import json
import validators
from urllib import request as rqst

# Create your views here.

@api_view(['POST'])
def home(request):
    component_name = request.POST.get('componentName')
    valid = validators.url(component_name)
    print(valid)
    # brand_name = request.data.get('brandName')
    print(component_name)
    # if valid==False:
    baseurl = "https://www.startech.com.bd/component/"
    # baseurl+str(component_name).lower()/// baseurl+str(component_name)
    print()
    return HttpResponse(scrapcomponents(component_name))
    
@api_view(['POST'])
def fetchbybrands(request):
    component_name = request.POST.get('brandurl')

    baseurl = "https://www.startech.com.bd/component/"

    return HttpResponse()


def scrapcomponents(baseurl):
    page = rqst.urlopen(baseurl)
    soup = BeautifulSoup(page, "html.parser")
    main_contents = soup.find("div", {"class": "row main-content"})
    list_of_home_contents = main_contents.findAll("div", {"class": "product-thumb"})
    context = []


    for content in list_of_home_contents:
        image = content.find(class_="img-holder").find("img")
        name = content.find(class_="product-info").find(class_="product-name").find('a').get_text()
        price = content.find(class_="actions").find(class_="price space-between").find('span').get_text()
        urls = content.find(class_="img-holder").find("a")
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
    component_name = request.POST.get('componentName')
    print(component_name)
    baseurl = "https://www.startech.com.bd/component/"
    # baseurl+str(component_name).lower()
    page = rqst.urlopen(component_name)
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
def brandscomponents(request):
    casing = "https://www.startech.com.bd/component/casing"
    processor = "https://www.startech.com.bd/component/processor"
    brand_url = request.POST.get('brandurl')
    page = rqst.urlopen(brand_url)
    soup = BeautifulSoup(page, "html.parser")
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
    page = rqst.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    container = soup.find("div", {"class": "row clearfix"})
    main_container = container.findAll("div", {"class": "col-md-6"})
    img = main_container[0].find(class_="images product-images").find('a')
    # print(img['href'])
    name = main_container[1].find(class_="product-short-info").find('h1').get_text()
    # print(name)
    price = main_container[1].find(class_="product-short-info").find(class_="product-info-data product-price").get_text()
    ul = main_container[1].find(class_="short-description").find('ul')
    features = []
    for lis in ul.findAll('li'):
        features.append(lis.get_text())

    description = soup.find("section", {"id": "description"})
    # desc = description.find('p').get_text()
    desc = description.find("div" , {"itemprop": "description"})
    print(desc.get_text())

    # print(features)
    mainjson = []


    con = {
        "img": img['href'],
        "name": name,
        "price": price,
        "features": features,
        "description": desc.get_text()
    }
    mainjson.append(con)
    jformat = json.dumps(con)
    return HttpResponse(jformat)

