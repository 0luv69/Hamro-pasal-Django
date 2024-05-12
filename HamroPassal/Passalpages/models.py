from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    ratting= models.IntegerField()
    amount= models.FloatField()
    sale= models.BooleanField(default=False)
    image= models.ImageField(upload_to="media")
  


class carts_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_items= models.IntegerField(default=0)

class itemsInCart(models.Model):
    cart_info= models.ForeignKey(carts_info, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class CheckOutInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Phonenum=models.IntegerField(null=True, blank=True)
    shipemail= models.EmailField()
    Order_Notes=  models.CharField(max_length=350, null=True, blank=True)
    
    Country= models.CharField(max_length=50)
    State= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    Street_Name= models.CharField(max_length=50)
    Full_Address= models.CharField(max_length=300)

class shipping_info(models.Model):
    checkout_info = models.ForeignKey(CheckOutInfo, on_delete=models.CASCADE)
    shipping_number= models.CharField(max_length=100)
    ordered_Date= models.DateField(auto_now_add=True)
    deliver_Date_on= models.DateField(null=True)
    recived_items= models.BooleanField(default=False)
    paid_money= models.BooleanField(default=False)

class checkout_products(models.Model):
    shippinginfo= models.ForeignKey(shipping_info, on_delete=models.CASCADE)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)    