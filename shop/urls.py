
from django.urls import path, include
from .views import home, products, about_us

urlpatterns = [
 path("",'home/', home, name='home_page'),
 path('products/', products, name='products_page'),
 path('about_us/', about_us, name='about_us_page'),
 
]