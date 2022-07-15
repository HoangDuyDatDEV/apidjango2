
from django.urls import path
from .Controler.UserController import *
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(),name= 'login'),
    path('logout/', Logout.as_view(), name='logout'),
]