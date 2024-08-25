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
  path('deletecategory/<int:category_id>',deleteCategory),
  path('updatecategory/<int:category_id>',updateCategory),
  path('deleteproduct/<int:product_id>',deleteProduct),
  path('updateproduct/<int:product_id>',updateProduct),
  
]