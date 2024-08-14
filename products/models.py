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