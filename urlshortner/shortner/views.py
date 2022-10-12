from multiprocessing import context
from django.shortcuts import render
from urllib3 import HTTPResponse

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    return render(request, 'login.html')

def go(request, url):
     return render (request,'form.html', context={
         'url':url,
     })
     
