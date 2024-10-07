from django.db import models
#from djmoney.models.fields import MoneyField
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=5)
    class_number = models.CharField(max_length=9) 
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} {self.class_number}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    
class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='upload/book/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=14, decimal_places=0, default=0)

    def __str__(self):
        return self.name