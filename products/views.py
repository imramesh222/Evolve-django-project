from django.shortcuts import render

from .models import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def allproduct(request):
    context={
        'product':Product.objects.all()
    }
    return render(request,'pages/allproducts.html',context)

def all_product(request):
    context={
        'p_product':P_product.objects.all()
    }
    return render(request,'pages/all_products.html',context)
    