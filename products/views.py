from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def homepage(request):
    # return HttpResponse("This is the homepage")
    return render(request, 'homepage.html')

def allproduct(request):
    context={
        'product':Product.objects.all()
    }
    return render(request,'pages/allproducts.html',context)