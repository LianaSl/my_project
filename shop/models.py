from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

   

    def __str__(self):
        return self.name

class User(AbstractUser):
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=10000.00,
        verbose_name="Баланс"
    )

    def __str__(self):
        return self.username


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    is_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='shop/products/',blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', blank=True, null=True)


    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


    def __str__(self):
        return self.name

    # image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # def __str__(self):
    #     return self.name2