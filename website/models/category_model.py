from django.db import models
from .product import Product

class Category(models.Model):
    """
    purpose: Creates Category table within database
        Example useage:

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    category_name = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.category_name

    def get_products(self):
        print(dir(self))
        return Product.objects.filter(product_category=self)
