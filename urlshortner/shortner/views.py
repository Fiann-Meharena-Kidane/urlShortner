from multiprocessing import context
from random import random, choice
import re
import string
from django.shortcuts import redirect, render
from urllib3 import HTTPResponse
from . models import Url

# Create your views here.

def index(request):
    if request.method=='POST':
        link=request.POST['link']
        short_link='http://127.0.0.1:8000/go/'
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in range(6):
            short_link+=choice(letters)
            
        new_link=Url(original_link=link,
                     short_link=short_link)
        
        new_link.save()
        
        return render(request, 'index.html', {'link':link, 'short_link':short_link})
        # return redirect('login')
    else:
        return render(request,'index.html')


def login(request):
    return render(request, 'login.html')


def go(request, url):
    
    short_link='http://127.0.0.1:8000/go/'+url
    original_link=Url.objects.get(short_link=short_link)
     
    return render (request,'form.html', context={
         'url':original_link.original_link,
    
     })
     
