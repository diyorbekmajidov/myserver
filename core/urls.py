from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from myapp.views import add,get_company,get_products,get_RAM,get_products_by_color,get_products_by_price,get_products_by_img,get_products_by_name

def main(request):
    return HttpResponse("<h1>Hello world</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add),
    path('get_products', get_products),
    # path('',home),
    path('get_company/<str:company>', get_company),
    path("get_RAM/<str:RAM>", get_RAM),
    path('get_products_by_color/<str:color>', get_products_by_color),
    path('get_products_by_price/<str:price>', get_products_by_price),
    path('get_products/get_products_by_img/<str:img_url>', get_products_by_img),
    path('get_products_by_name/<str:name>', get_products_by_name),
]
