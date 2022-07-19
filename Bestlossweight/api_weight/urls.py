
from django.urls import path
from api_weight.Controler.PlanController import handleCreatePlan

from api_weight.DAO.PlanDAO import CreatePlan
from .Controler.UserController import *
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(),name= 'login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('addPlan/',handleCreatePlan,name='createPlan')
]