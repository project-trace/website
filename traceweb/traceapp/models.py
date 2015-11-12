from django.db import models

class Item(models.Model):
    device_id = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')
    name = models.CharField(max_length=200)
    

# Create your models here.
