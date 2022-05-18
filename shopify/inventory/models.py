from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'Location:{self.location}'

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Name:{self.name}, Price:{self.price}'
