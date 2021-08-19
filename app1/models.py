from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    contact_no=models.IntegerField(unique=True)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=32,unique=True)
    username=models.CharField(max_length=32,unique=True)
class Login(models.Model):
    username=models.CharField(max_length=32,unique=True)
    password=models.CharField(max_length=32)
    type=models.CharField(max_length=10)