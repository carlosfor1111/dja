from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    receipt_id = models.IntegerField(null=True, blank=True)
    receipt_date = models.DateField(default=date.today,null=True, blank=True)
    receipt_pic = models.ImageField(null=True,blank=True)
    inspection_pic = models.ImageField(null=True,blank=True)
    inspection_id = models.IntegerField(null=True, blank=True)
    inspection_group = models.CharField(max_length=200, null=True, blank=True)
    inspection_date = models.DateField(default=date.today,null=True, blank=True)
    inspection_doctor = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(default=date.today,null=True, blank=True)
    height = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    sales_name = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)   

    def __str__(self):
       return str(self.receipt_id)       
