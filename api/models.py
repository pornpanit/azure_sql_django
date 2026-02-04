from datetime import timezone
from django.db import models

# Create your models here.

class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    product_detail = models.CharField(max_length=1000)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.product_detail} - {self.product_price}"
    
class User(models.Model):
    user_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.user_id} - {self.user_name} - {self.user_email}"