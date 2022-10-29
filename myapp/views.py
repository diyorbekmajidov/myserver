from itertools import product
from math import prod
import re
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from multiprocessing import context
from .models import Product
# Create your views here.

def convert_to_json(product):
    product_json = {
        'id': product.id,
        'name': product.name,
        'company': product.company,
        'color': product.color,
        'RAM': product.RAM,
        'memory': product.memory,
        'price': product.price,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'img_url': product.img_url,
    }
    return product_json

def get_products(request):
    products = Product.objects.all()
    products_json = []
    for product in products:
        products_json.append(convert_to_json(product))
    return JsonResponse({'products': products_json})


def add(request):
    POST=request.POST  
    db=Product(
        name=request.POST['name'],
        company=request.POST['company'],
        color=request.POST['color'],
        RAM=request.POST['RAM'],
        memory=request.POST['memory'],
        price=request.POST['price'],
        img_url=request.POST['img_url'],
    )
    db.save()
    return JsonResponse({'ok':True})

def get_company(reqiest,gre):
    if reqiest.method=='GET':
        products = Product.objects.filter(company=gre)
        products1=Product.objects.values('company')
        products_json = []
        product_set=set()
        for product in products:
            products_json.append(convert_to_json(product))
            
        for i in products1:
            product_set.add(i['company'])
        context ={'data1':products_json,"data":list(product_set)}

    return render(reqiest, 'index.html',context=context)

def get_RAM(reqiest,RAM):
    if reqiest.method=='GET':
        products=Product.objects.filter(RAM__icontains=RAM)
        products_json=[]
        for product in products:
            products_json.append(convert_to_json(product))

        context={'data1':products_json}
    return render(reqiest, 'index.html',context=context)

def get_products_by_color(reqiest,color):
    if reqiest.method=='GET':
        products=Product.objects.filter(color__icontains=color)
        products_json=[]
        for product in products:
            products_json.append(convert_to_json(product))

        context={'data1':products_json}
    return render(reqiest, 'index.html',context=context)

def get_products_by_price(reqiest,price):
    if reqiest.method=="GET":
        products=Product.objects.filter(price__icontains=price)
        products_json=[]
        for product in products:
            products_json.append(convert_to_json(product))
        
        context={'data1':products_json}
    return render(reqiest, 'index.html', context=context)

def get_oraliq_price(reqiest,price):
    if reqiest.method=="GET":
        products=Product.objects.filter(id__gt=price)
        products_json=[]
        for product in products:
            products_json.append(convert_to_json(product))

        context={"data1":products_json}
    return render(reqiest, 'index.html', context=context)

def get_products_by_img(reqiest,img_url):
    if reqiest.method=="GET":
        products=Product.objects.filter(img__icontains=img_url)
        products_json=[]
        for product in products:
            products_json.append(convert_to_json(product))
        
        context={'data1':products_json}
    return render(reqiest, 'index.html', context=context)

def get_products_by_name(reqiest,name):
    if reqiest.method=="GET":
        products=Product.objects.filter(name__icontains=name)
        products_json=[]
        for product in products:
            products_json.append(convert_to_json(product))
        
        context={'data1':products_json}
    return render(reqiest, 'index.html', context=context)

def companyes(requiest):
    if requiest.method=="GET":
        products=Product.objects.values('company')
        product_set=set()
        for i in products:
            product_set.add(i['company'])
        
        context={"data":list(product_set)}
        return render(requiest, 'url.html', context=context)

