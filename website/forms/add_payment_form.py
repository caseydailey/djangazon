from django import forms
from website.models import PaymentType

class AddPaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ('name', 'account_number')
