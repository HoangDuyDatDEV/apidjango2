from typing import Type
from django.db import models

# Create your models here.
class User (models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    Adrress=models.CharField(max_length=500)
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=15)
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    Type= models.CharField(max_length=100)
    Name=models.CharField(max_length=200)
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    Amount=models.IntegerField()
    Date=models.DateField()
    Location=models.CharField(max_length=500)
    Photo= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    UserID=models.ForeignKey(User,on_delete=models.CASCADE)    
    CategoryID=models.ForeignKey(Category,on_delete=models.CASCADE)  

    