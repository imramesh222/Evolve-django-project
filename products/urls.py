from django.urls import path
from .views import *
# from . import views


urlpatterns =[
  path('',homepage,name='homepage'),
  path('addproducts',addProduct),
  path('allproducts',allproduct),
  path('all_products',all_product),
  path('addcategory',addCategory),
  path('allcategory',allCategory),
  
]