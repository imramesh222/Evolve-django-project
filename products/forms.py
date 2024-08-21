from django.forms import ModelForm
from .models import *



class CategoryForm(ModelForm):
  class Meta:
    model=Category
    fields='__all__'


class ProductForm(ModelForm):
  class Meta:
    model=Product
    fields='__all__'
