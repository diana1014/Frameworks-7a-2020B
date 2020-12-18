from django.db import models

# Create your models here.

class Category (models.Model):
    code= models.CharField(max_length=20)
    name= models.CharField(max_length=100)
    status= models.BooleanField(default=True)
    description=models.CharField(default='Description here', max_length=20)
    create_date= models.DateTimeField(auto_now=True)
    update_date= models.DateTimeField(auto_now=True)

class Vendor(models.Model):
    code= models.CharField(max_length=20)
    name= models.CharField(max_length=100)
    status= models.BooleanField(default=True)
    description=models.TextField(default='Description here')

class Products (models.Model):
    code= models.CharField(max_length=10)
    name= models.CharField(max_length=100)
    unit_price=models.IntegerField()
    quantity=models.IntegerField()
    id_category= models.ForeignKey(Category,on_delete= models.CASCADE )
    id_vendedor= models.ForeignKey(Vendor,on_delete= models.CASCADE )
    status= models.BooleanField(default=True)
    create_date= models.DateTimeField(auto_now=True)
    update_date= models.DateTimeField(auto_now=True)

class Stock (models.Model):
    code= models.CharField(max_length=10)
    id_product= models.ForeignKey(Products,on_delete= models.CASCADE)
    quantity=models.IntegerField()
    update_date= models.DateTimeField(auto_now=True)
    description=models.TextField(default='Description here')
