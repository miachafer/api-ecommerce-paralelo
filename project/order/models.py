from django.db import models
from project.client.models import Client
from project.product.models import Product

class Order(models.Model):
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.description}'

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f'Order: {self.order_number} - Client: {self.client} - Product: {self.product} - Quantity: {self.quantity}'

    