from django.db import models

# Create your models here.

class Url(models.Model):
    original_link=models.CharField(max_length=10000)
    short_link=models.CharField(max_length=1000)
    