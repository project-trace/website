from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Device(models.Model):
	name = models.CharField(max_length=200, primary_key=True)
	des = models.CharField(max_length=200, default="")
	device_id = models.CharField(max_length=200, default="")
	img = models.CharField(max_length=200, default="static/traceapp/img/item.png")
	enabled = models.CharField(max_length=1, default="1")
	button = models.CharField(max_length=200, default="Disable")
	style = models.CharField(max_length=200, default="")

