from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Device(models.Model):
    name = models.CharField(max_length=200, unique=True)    
    device_id = models.CharField(max_length=200, unique=True)

