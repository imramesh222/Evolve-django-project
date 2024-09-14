from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
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
