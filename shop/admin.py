from django.contrib import admin
from .models import Products

class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_stock')
    search_fields = ('name', 'description')
    list_filter = ('is_stock','price' )

admin.site.register(Products, AdminProducts, )

# Register your models here.
