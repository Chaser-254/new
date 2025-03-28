from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.

# class Employees(models.Model):
#     code = models.CharField(max_length=100,blank=True) 
#     firstname = models.TextField() 
#     middlename = models.TextField(blank=True,null= True) 
#     lastname = models.TextField() 
#     gender = models.TextField(blank=True,null= True) 
#     dob = models.DateField(blank=True,null= True) 
#     contact = models.TextField() 
#     address = models.TextField() 
#     email = models.TextField() 
#     department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
#     position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
#     date_hired = models.DateField() 
#     salary = models.FloatField(default=0) 
#     status = models.IntegerField() 
#     date_added = models.DateTimeField(default=timezone.now) 
#     date_updated = models.DateTimeField(auto_now=True) 

    # def __str__(self):
    #     return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code + " - " + self.name

class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)

class inventory(models.Model):
    name = models.TextField()
    description = models.TextField()
    Quantity_Available = models.IntegerField(default=0)

    def __str__(self):
        return self.code + " - " + self.name

class Stock(models.Model):
    stock_code = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=255)
    units_of_measure = models.CharField(max_length=50)
    quantity_available = models.PositiveIntegerField()
    recorded_value = models.PositiveBigIntegerField()
    factory_price = models.DecimalField(max_digits=10,decimal_places=2)
    wholesale_pice = models.DecimalField(max_digits=10,decimal_places=2)
    retail_prices = models.DecimalField(max_digits=10,decimal_places=2)
    supplier_prices = models.DecimalField(max_digits=10,decimal_places=2)
    product_supplier = models.CharField(max_length=255)

    def __str__(self):
        return self.description
    
    def is_below_reorder_level(self):
        return self.quantity_available <= self.recorded_value
    

class Debtors(models.Model):
    name = models.CharField(max_length=150)
    amount_owed = models.DecimalField(max_digits=10,decimal_places=2)
    date_owed = models.DateField()

    def __str__(self):
        return self.name
    
class Creditor(models.Model):
    name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return self.name