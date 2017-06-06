from django import forms
from website.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'product_category', 'city', 'local_delivery', 'image_path')
