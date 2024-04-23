from django.db import models

# Create your models here.

class NewUser(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    cardno = models.CharField(max_length=100)