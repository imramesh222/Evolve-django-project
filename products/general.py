from .models import *
def setting(request):
  data=Setting.objects.all()  # get all  from settings
  context={
    'data':data  # pass data to template
  }
  return context

# def product(request):
#   content={
#     'data':Product.objects.all()
#   }
#   return content