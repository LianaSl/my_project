from django.contrib import admin
from .models import Products, Category

class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_stock')
    search_fields = ('name', 'price')
    list_filter = ('price', 'quantity',)

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Products, AdminProducts)
admin.site.register(Category, AdminCategory)

# Register your models here.
 