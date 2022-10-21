from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from myapp.views import home

def main(request):
    return HttpResponse("<h1>Hello world</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
]
