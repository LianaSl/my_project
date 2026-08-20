from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        "name" : "LiANA",
        "age" : 50,
        "list" : [1,2,3,4,5,6,7,8,9,10],
        "tuple" : (1,2,3,4,5,6,7,8,9,10),
        "set" : {1,2,3,4,5,6,7,8,9,10},
        "dict" : {"city": "Prague"}

    }
    return render(request, "shop/home.html", context)

def products(request):
    return HttpResponse("Here are our products!")

def about_us(request):
    return HttpResponse("About us page.")
def hello(request, name):
    return HttpResponse(f"Hello, {name}!")

def product_detail(request, id):
    return HttpResponse(f"Product id({id})")
    /