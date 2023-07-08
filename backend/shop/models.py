from unicodedata import name
from django.db import models
from users.models import NewUser
from products.models import Product



class Inventory(models.Model):
    products = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    owner = models.ForeignKey(NewUser, related_name='owner', on_delete=models.RESTRICT)
    inventory = models.ForeignKey(Inventory, related_name='inventory', on_delete=models.CASCADE)

    def __str__(self):
        self.name




