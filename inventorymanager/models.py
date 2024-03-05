from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    locations = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=255)

    def __str__(self):
        return self.name
