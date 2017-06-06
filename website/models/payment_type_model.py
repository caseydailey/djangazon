from django.contrib.auth.models import User
from django.db import models

class PaymentType(models.Model):
    """
    purpose: Creates PaymentType table within database
        Example useage:

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.TextField(blank=True, null=False, max_length=50)
    account_number = models.IntegerField(range(12, 20))

    # def __str__(self):  # __unicode__ on Python 2
    #     return self.name
