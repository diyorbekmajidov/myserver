from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import context
# Create your views here.

def home(request):
    context={
        'username':'Javohir',
        'age':23,
        'list':[1,2,3,4,5,6,7,8,9]
    }
    return render(request, 'index.html',context=context)
