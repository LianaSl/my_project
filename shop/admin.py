from django.contrib import admin
from .models import Products

class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_stock')
    search_fields = ('name', 'description')

admin.site.register(Products)

# Register your models here.
