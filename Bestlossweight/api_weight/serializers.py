from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from api_weight.DAO.PlanDAO import CreatePlan

from api_weight.models import Plan




#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id","email", "username","password"]
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
#Plan
class PlanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Plan
        fields=('__all__')
    def createplan():
        res = CreatePlan(User.UserID,Plan.CurrentWeight,Plan.TargetWeight,Plan.TargetDate)
        return res
