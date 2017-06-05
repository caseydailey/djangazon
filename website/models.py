from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
    """
    purpose: Creates Category table within database
        Example useage:

    author: Taylor Perkins, Justin Short

    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(blank=True, null=False, max_length=15)
    address = models.TextField(blank=True, null=False, max_length=200)

    def __str__(self):  # __unicode__ on Python 2
        return self.user.first_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


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
        on_delete=models.CASCADE,
    )
    # django will display a dropdown with these choices
    CATEGORY_CHOICES = (
        ('electronics', 'ELECTRONICS'),
        ('sports', 'SPORTS'),
        ('home', 'HOME'),
        ('general', 'GENERAL'),
        ('clothing', 'CLOTHING')
    )
    product_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        choices=CATEGORY_CHOICES
    )
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

class LikeDislike(models.Model):
    """
    purpose: Creates Intermediate between to given Users and Products, to specify whether or not a user
    Likes or Dislikes a Product. 
    A product is liked when the user clicks like button on product_details, or they order that product

    author: Taylor Perkins


    args: models.Model: (NA): models class given by Django

    returns: (None): N/A
    """        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='preferrenced_product')
    liked = models.BooleanField()

    def __str__(self):
        if self.liked:
            return "like {}".format(self.product.title)
        return "dislike {}".format(self.product.title)

