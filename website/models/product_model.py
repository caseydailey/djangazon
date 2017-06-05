from django.contrib.auth.models import User
from django.db import models

from .category_model import Category

class Product(models.Model):
    """
    purpose: Creates Product table within database
        Example useage:

    author: Taylor Perkins, Justin Short, Casey Dailey

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    # django will display a dropdown with these choices
    CATEGORY_CHOICES = (
        ('electronics', 'ELECTRONICS'),
        ('sports', 'SPORTS'),
        ('home', 'HOME'),
        ('general', 'GENERAL'),
        ('clothing', 'CLOTHING'))

    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        choices=CATEGORY_CHOICES)

    quantity = models.IntegerField(null=False)
    description = models.TextField(null=False, max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date_created = models.DateField(auto_now=True, auto_now_add=False)  # This auto generates date on creation
    title = models.CharField(max_length=255)
    local_delivery = models.BooleanField(default=1)
    city = models.CharField(max_length=255)
    image_path = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title
