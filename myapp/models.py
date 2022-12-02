from django.db import models
from django.conf import settings

# Create your models here.
class contact1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    title=models.TextField(max_length=200)
    text=models.TextField(max_length=200)
   