from django.shortcuts import render,redirect
from django.contrib import messages

from .models import *
from .forms import *
# Create your views here.



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
            messages.add_message(request,messages.SUCCESS,'Category Added succesfully')
            return redirect('/allcategory')
        else:
            messages.add_message(request,messages.ERROR,'Category add unsuccesful')
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

def deleteCategory(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,("Item removed succesfully!!"))
    return redirect('/allcategory')
    

def updateCategory(request,category_id):
    cateData=Category.objects.get(id=category_id)

    if request.method=='POST':
        cateform=CategoryForm(request.POST,request.FILES,instance=cateData)
        if cateform.is_valid():
            cateform.save()
            messages.add_message(request,messages.SUCCESS,'Changed made succesfully')
            return redirect('/allcategory')
        else:
            messages.add_message(request,messages.ERROR,'Changed made unsuccessful')
            return redirect('/allcategory')
    context={
        'catForm':CategoryForm(instance=cateData)

    }
    return render(request,'pages/updatecategory.html',context)

def deleteProduct(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,('Product deleted'))
    return redirect('/allproducts')

def updateProduct(request,product_id):
    prodData=Product.objects.get(id=product_id)
    if request.method=='POST':
        cateform=ProductForm(request.POST,request.FILES,instance=prodData)
        if cateform.is_valid():
            cateform.save()
            messages.add_message(request,messages.SUCCESS,'Changed made succesfully')
            return redirect('/allproducts')
        else:
            messages.add_message(request,messages.ERROR,'Changed made unsuccessful')
            return redirect('/allproducts')

    context={
        'prodForm':ProductForm(instance=prodData)
    }
    return render(request,'pages/updateproduct.html',context)

# def update(request,product_id):
    productData=Product.objects.get(id=product_id)

    if request.method=="POST":
        prodform=ProductForm(request.POST,request.FILES,instance=productData)
        if prodform.is_valid():
            prodform.save()
            messages.add_message(request,messages.SUCCESS,'Hello girl')
            return redirect('/allproducts')
        else:
            messages.add_message(request,messages.ERROR,'Hello Boy')
            return request('/allproducts')
        
        context={
            'prodform':Pro
        }