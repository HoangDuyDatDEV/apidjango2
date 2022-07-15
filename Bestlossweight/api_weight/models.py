from django.db import models

# Create your models here.
class User (models.Model) :
    name = models.CharField(max_length=200)
    DOB= models.DateField()
    Adrress=models.CharField(max_length=500)
    Email=models.EmailField()
    Sex=models.CharField(max_length=10)
    Weight=models.IntegerField()
    height=models.IntegerField()
    Username=models.CharField(max_length=200)
    Password=models.CharField(max_length=15)
class Plan(models.Model):
    CurrentWeight = models.IntegerField()
    TargetWeight=models.IntegerField()
    TargetDate=models.DateTimeField()
    WeeklyRate=models.DecimalField(max_digits=10,decimal_places = 2)
    NumberTrainingPerWeek=models.IntegerField()
    BMR=models.DecimalField(max_digits=10,decimal_places = 2)
    UserID=models.ForeignKey('User',on_delete=models.CASCADE)      
class Meal(models.Model):
    Type=models.CharField(max_length=50)
    Food=models.CharField(max_length=100)
    FoodServing=models.CharField(max_length=150)
    AmountEaten=models.IntegerField()
    CaloriesFoodServing=models.IntegerField()
    CaloriesFood=models.IntegerField()
    TotalCalories=models.IntegerField()
    UserID=models.ForeignKey('User',on_delete=models.CASCADE)
