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
import time
from urllib.request import Request,urlopen
# Create your views here.


# @api_view(['POST'])
def home(request):
    baseurl = "https://www.techlandbd.com/pc-components"
    # component_name = request.POST.get('componentName')
    return HttpResponse(scrapcomponents(baseurl))
    
@api_view(['POST'])
def fetchbybrands(request):
    component_name = request.POST.get('brandurl')
    return HttpResponse()


def scrapcomponents(baseurl):
    tm = time.time()
    req = Request(baseurl, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    # print(soup)
    container = soup.find("div", {"class": "main-products product-grid"})
    list_of_home_contents = container.findAll("div", {"class": "product-thumb"})
    context = []

    for content in list_of_home_contents:
        img = content.find(class_="image").find(class_="product-img")['href']
        name = content.find(class_="caption").find(class_="name").find('a').get_text()
        url = content.find(class_="caption").find(class_="name").find('a')['href']
        price = content.find(class_="caption").find(class_="price-tax").get_text()
        replace_arr = ["Ex","Tax:"]
        price = price.replace("Ex Tax:","")
        print(price)

        con = {
            "images": img,
            "name": name,
            "price": price,
            "urls": url
        }
        context.append(con)
    context_json = json.dumps(context)
    print(time.time()-tm)
    return context_json


# @api_view(['POST'])
def brands(request):
    component_name = request.POST.get('componentName')
    baseurl = "https://www.techlandbd.com/pc-components/computer-casing"
    tm = time.time()
    req = Request(baseurl, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    # print(soup)
    container = soup.find("div", {"class": "refine-categories refine-grid"})
    list_of_components = container.find("div", {"class": "refine-items"}).findAll(class_="refine-item")
    com_list = []
    for component in list_of_components:
        name = component.find(class_="refine-name").get_text()
        url = component.find('a')['href']
        con = {
            "name": name,
            "link": url
        }
        com_list.append(con)
    brand_json = {
            "brands": com_list
        }
    brand_json = json.dumps(brand_json)
    print(time.time()-tm)
    return HttpResponse(brand_json)




# @api_view(['POST'])
def brandsAndComponentsName(request):
    burl = "https://"
    """ name = request.POST.get('name')
    print(name)
    shopobj = Shopsinfo.objects.get(shopename=name)
    url = shopobj.shopaddress
    print(url)
    url+="/component/"
    burl+=url"""
    baseurl = "https://www.techlandbd.com/pc-components"
    tm = time.time()
    req = Request(baseurl, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")
    # print(soup)
    container = soup.find("div", {"class": "refine-categories refine-grid"})
    list_of_components = container.find("div", {"class": "refine-items"}).findAll(class_="refine-item")
    com_list = []
    for component in list_of_components:
        name = component.find(class_="refine-name").get_text()
        url = component.find('a')['href']
        con = {
            "name": name,
            "link": url
        }
        com_list.append(con)
    brand_json = {
            "brands": com_list
        }
    brand_json = json.dumps(brand_json)
    print(time.time()-tm)
    return HttpResponse(brand_json)



# @api_view(['POST'])
def brandscomponents(request):
    # brand_url = request.POST.get('brandurl')
    url = "https://www.techlandbd.com/pc-components/computer-casing/aigo-case"
    return HttpResponse(scrapcomponents(url))

@api_view(['POST'])
def componentsdeatils(request):
    url = request.POST.get('url')
    print(url)
    jformat = json.dumps(components_in_details(url))
    return HttpResponse(jformat)

def components_in_details(url):
    con = {
    }
    return con