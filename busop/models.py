from django.db import models

# Create your models here.
class Busop(models.Model):
    username = models.CharField(max_length=50)
    phone=models.IntegerField()
    password = models.CharField(max_length=50)
    
    