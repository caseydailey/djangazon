from django.contrib.auth.models import User
from django.db import models

from .payment_type_model import PaymentType

class Order(models.Model):
    """
    purpose: Creates Order table within database
        Example useage:

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    date_complete = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)  # This will get filled upon order completion
