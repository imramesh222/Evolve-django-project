from django.db import models

# Create your models here.
class Setting(models.Model):
  title=models.CharField(max_length=200)
  favicon=models.CharField(max_length=500)
  logo=models.CharField(max_length=500)
  contact=models.IntegerField()
  email=models.EmailField(max_length=200)
  address=models.CharField(max_length=200)
  description=models.CharField(max_length=1000,null=True,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title

class Category(models.Model):
  name=models.CharField(max_length=200,null=True)
  description=models.TextField(max_length=1000,blank=True)
  created_at=models.DateTimeField(auto_now_add=True,null=True)

  def __str__(self):
    return self.name
class Product(models.Model):
  category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
  name=models.CharField(max_length=200)
  image=models.CharField(max_length=1000)
  price=models.DecimalField(max_digits=10,decimal_places=2)
  rating=models.DecimalField(max_digits=10,decimal_places=2)
  quantity=models.IntegerField()
  description=models.TextField(max_length=1000,null=True,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
  
class P_product(models.Model):
  name=models.CharField(max_length=200)
  image=models.CharField(max_length=1000)
  price=models.DecimalField(max_digits=10,decimal_places=2)
  rating=models.DecimalField(max_digits=10,decimal_places=2)
  quantity=models.IntegerField()
  description=models.TextField(max_length=1000,null=True,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name


