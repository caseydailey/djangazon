from django.db import models

from .product_model import Product
from .order_model import Order

class UserOrder(models.Model):
    """
    purpose: Creates Intermediate table between Order and Product within database
        Example useage:

    author: Taylor Perkins

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
