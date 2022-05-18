from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    sales = models.IntegerField()
    in_stock = models.BooleanField()
    quantity = models.IntegerField()
    deletion_comment = models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name}, Price:{self.price}, Quantity:{self.quantity}'
