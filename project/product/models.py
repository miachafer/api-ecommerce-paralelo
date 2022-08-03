from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(
        default=0.00, 
        max_digits=10, 
        decimal_places=2,
        blank=False,
        validators=[MinValueValidator(0.01)],
        help_text="Type the price in the format: 0.00")
    quantity = models.IntegerField(
        default=0,
        blank=False,
        validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.price} - {self.quantity} available"
    
