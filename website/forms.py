from django.contrib.auth.models import User
from django import forms
from website.models import Product, PaymentType, Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):  

    class Meta:
        model = Profile
        fields = ('phone_number', 'address')

class ProductForm(forms.ModelForm): 

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'product_category', 'city', 'local_delivery')

class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ('name', 'account_number')


