from django.contrib.auth.models import User
from django.db import models

from .product import Product

class Recommendations(models.Model):
    """
    purpose: Creates Intermediate between to given Users, as well as Product to User.

    author: Taylor Perkins

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    to_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_people')
    from_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_people')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=0)
