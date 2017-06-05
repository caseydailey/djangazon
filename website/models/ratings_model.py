from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .product_model import Product

class Ratings(models.Model):
    """
    purpose: Creates an intermediate table to store user ratings for products

    author: casey dailey

    args: models.Model

    returns: n/a
    """

    user = models.ForeignKey(User, default=None)    
    product = models.ForeignKey(Product)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5),
                                             MinValueValidator(0)])

    def __str__(self):
        return self.product.title
