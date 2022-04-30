from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=23)
    
class Category(models.Model):
    name = models.CharField(max_length=534)
    
    def __str__(self):
        return self.name
    


class Color(models.Model):        
    name = models.CharField(max_length=46)
    code = models.CharField(max_length=46)
    
    

class Filter_Price(models.Model):
    prices = (
        ("500 TO 3000","500 TO 3000"),
        ("3000 TO 5000","3000 TO 5000"),
        ("5000 TO 10000","5000 TO 10000"),
        ("10000 TO 15000","10000 TO 15000"),
        ("15000 TO 20000","20000 TO 20000"),
        ("20000 TO 30000","500 TO 30000"),
        ("20000 TO 50000","20000 TO 50000"),
        ("50000 TO 100000","50000 TO 100000")
    )
    price = models.CharField(choices=prices,max_length=46)    
        
    
    
class Product(models.Model):
    choicesc = (
        ("new","new"),
        ("old","old")
    )
    schoices =(
        ("publish","publish"),
        ("hide","hide")
    )
    name = models.CharField(max_length=57)
    price = models.CharField(max_length=57)
    category = models.CharField(max_length=57)
    information = RichTextField()
    description =RichTextField()
    name = models.CharField(max_length=57)
    image = models.ImageField(upload_to="komal")
    condition = models.CharField(choices=choicesc, max_length=46)
    stock = models.CharField(choices=schoices,max_length=35465)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,default=1)
    
    
    

class Tag(models.Model):
    name = models.CharField(max_length=46)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
        
        
class images(models.Model):
    name = models.ImageField(upload_to = "komal")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
                
                
                
class Contact(models.Model):
    name = models.CharField(max_length=57)
    email = models.EmailField(max_length=57)
    subject = models.CharField(max_length=57)
    imformation =models.TextField(default="teteteteterterterte")
    
    
class Orderform(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete= models.CASCADE)
    firstname= models.CharField(max_length=57)
    lastnam = models.CharField(max_length=57)
    country= models.CharField(max_length=57,default="india")
    housnum= models.CharField(max_length=57)
    city= models.CharField(max_length=57)
    state  = models.CharField(max_length=57)  
    zipcode = models.CharField(max_length=57)
    phone= models.CharField(max_length=57)
    email= models.CharField(max_length=57)
    additninal= models.CharField(max_length=57)
    price= models.CharField(max_length=57)
    quntity= models.CharField(max_length=57)
                      
                
    def __str__(self):
        return self.firstname
   
   
   
   
class Team(models.Model):
    name = models.CharField(max_length=57)
    skill = models.CharField(max_length=57)
    email = models.EmailField(max_length=57)
    teammemberimg =  models.ImageField(upload_to = "komal")
    teaminfo =models.TextField(default="teteteteterterterte") 
    
    
    def __str__(self):
        return self.name
    