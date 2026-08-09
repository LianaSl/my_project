from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the shop!")

def products(request):
    return HttpResponse("Here are our products!")

def about_us(request):
    return HttpResponse("About us page.")
def hello(request, name):
    return HttpResponse(f"Hello, {name}!")