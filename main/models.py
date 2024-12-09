from django.db import models

# Create your models here.

# models.py
class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Unknown")


    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.name
