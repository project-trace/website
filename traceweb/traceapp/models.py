from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Item(models.Model):
    name = models.CharField(max_length=200)    
    description = models.TextField() 
    device_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=datetime.now)
    signal_strength = models.CharField(max_length=200)

# Create your models here.
