from django.urls import path
from .views import *
# from . import views


urlpatterns =[
  path('',homepage,name='homepage'),
  path('allproducts',allproduct)
  
]