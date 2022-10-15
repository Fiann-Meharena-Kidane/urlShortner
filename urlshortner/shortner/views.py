from multiprocessing import context
from random import random, choice
import re
import string
from django.shortcuts import redirect, render
from urllib3 import HTTPResponse
from . models import Url 
import datetime

# Create your views here.
year=datetime.datetime.now().year


def index(request):
    
    if request.method=='POST':
        link=request.POST['link']
        short_link='http://127.0.0.1:8000/go/'
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        all_link_objects=Url.objects.all()
        all_links=[object.original_link for object in all_link_objects]
        
        if not link in all_links: # if its new link, 
            for i in range(6):
                short_link+=choice(letters)
            
            new_link=Url(original_link=link,
                        short_link=short_link)
            new_link.save()
            
            return render(request, 'index.html', {'link':link, 'short_link':short_link, 'year':year})
        
        else: # if its old link, just return the saved link from db, 
            
            my_url=Url.objects.get(original_link=link)
            return render(request, 'index.html', {'link':link, 'short_link':my_url.short_link , 'year':year} )
             
    else:
        return render(request,'index.html', {'year':year})


def login(request):
    return render(request, 'login.html')


def go(request, url):
    
    short_link='http://127.0.0.1:8000/go/' + url
    original_link=Url.objects.get(short_link=short_link)
    
    # return redirect(original_link.original_link)  # easiest way, just redirect to the actual url, 
     
    # bit complex way, pass actual url to an html          page,then auto click it using js.
    return render (request,'form.html', context={ 'year':year    
    
     })
     
