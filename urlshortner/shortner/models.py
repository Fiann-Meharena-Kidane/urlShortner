from django.db import models

# Create your models here.

class Url(models.Model):
    original_link=models.CharField(max_length=10000)
    short_link=models.CharField(max_length=1000)
    
    
    def __str__(self):
        return 'demo_link'