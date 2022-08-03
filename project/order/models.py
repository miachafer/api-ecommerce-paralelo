from django.db import models
from project.client.models import Client
from project.product.models import Product
from django.core.validators import MinValueValidator

class Order(models.Model):
    description = models.TextField(blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.id} - Description: {self.description}"

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    quantity = models.IntegerField(
        # default = 0,
        blank=False,
        validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.id} - Order_related: {self.order} - Product: {self.product} - Quantity: {self.quantity}"

    