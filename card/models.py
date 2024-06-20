from django.db import models
from store.models import Products
# Create your models here.
class Card(models.Model):
    session_user=models.CharField(max_length=100,unique=True)


class CardItem(models.Model):
    card=models.ForeignKey(Card, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Products, on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    price=models.FloatField(null=True)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.title
    


class Order(models.Model):
    city = models.TextField()
    street = models.TextField()
    home = models.TextField()
    flot = models.CharField(max_length=20)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT,null=True, default=None)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)