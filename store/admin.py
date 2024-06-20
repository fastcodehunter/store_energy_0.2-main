from django.contrib import admin
from store.models import Products
from card.models import Order,OrderItem
from django.contrib.sessions.models import Session


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','title','price','preview','quantity']
    
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','surname','email']
    inlines = [OrderItemInline]