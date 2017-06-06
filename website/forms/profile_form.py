from django import forms
from website.models import Profile

class ProfileForm(forms.ModelForm):  

    class Meta:
        model = Profile
        fields = ('phone_number', 'address')

