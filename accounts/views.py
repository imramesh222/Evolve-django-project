from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import*
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def register(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.add_message(request,messages.SUCCESS,'User register succesfully')
      return redirect('/',{'Form':form})
    else:
      messages.add_message(request,messages.ERROR,'User register failed.')
      return render(request,'register.html',{'Form':form})
  context={
    'Form':UserCreationForm()
  }
  return render(request,'register.html',context)


# UserLogin

def userLogin(request):
  if request.method=="POST":
    form=LoginForm(request.POST)
    if form.is_valid():
      data=form.cleaned_data
      user=authenticate(request,username=data['username'],password=data['password'])
      if user is not None:
        login(request,user)
        messages.add_message(request,messages.SUCCESS,"Login succesful.")
        return redirect('/')
      else:
        messages.add_message(request,messages.ERROR,"Invalid Credentials.")
        return render(request,'login.html',{'Forms':form})
  context={
    'Forms':LoginForm()
  }
  return render(request,'login.html',context)

def userLogout(request):
  logout(request)
  messages.add_message(request,messages.SUCCESS,'Logout successful.')
  return redirect('/')