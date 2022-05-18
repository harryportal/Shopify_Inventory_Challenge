from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Name:{self.name}'

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    sales = models.IntegerField()
    in_stock = models.BooleanField(default=False)
    quantity = models.IntegerField()
    deletion_comment = models.CharField(max_length=100)
    deleted = models.BooleanField(default=False)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)


    def __str__(self):
        return f'Name: {self.name}, Price:{self.price}, Quantity:{self.quantity}'