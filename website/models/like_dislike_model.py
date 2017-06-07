from django.contrib.auth.models import User
from django.db import models

from .product_model import Product

class LikeDislike(models.Model):
    """
    purpose: Creates Intermediate between to given Users and Products, 
             to specify whether or not a user Likes or Dislikes a Product. 
             A product is liked when the user clicks like button on product_details, 
             or they order that product

    author: Taylor Perkins

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='preferrenced_product')
    liked = models.BooleanField()

    def __str__(self):
        if self.liked:
            return "liked {}".format(self.product.title)
        return "disliked {}".format(self.product.title)

