from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
from .forms import *
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def addProduct(request):
    if request.method=='POST':
        prodform=ProductForm(request.POST,request.FILES)
        if prodform.is_valid():
            prodform.save()
            return redirect('/allproducts')
        else:
            messages(request.messages,'Failed adding Product')
            return render(request,'addproduct.html',{'prodForm':context})


    context={
        'prodForm':ProductForm()
    }
    return render(request,'pages/addproduct.html',context)


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

def addCategory(request):
    if request.method=='POST':
        catform=CategoryForm(request.POST)
        if catform.is_valid():
            catform.save()
            return redirect('/allcategory')
        else:
            return render(request,'addcategory.html',{'catForm':context})
    context={
        'catForm':CategoryForm()
    }
    return render(request,'pages/addcategory.html',context)
    
def allCategory(request):
    context={
        'category':Category.objects.all()
    }
    return render(request,'pages/allcategory.html',context)