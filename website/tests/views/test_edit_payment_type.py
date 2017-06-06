from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from website.models import PaymentType

class TestEditPaymentType(TestCase):

    def setUp(self):

        self.user_one = User.objects.create(username="test1", 
                password="test123")
        self.user_two = User.objects.create(username="test2", 
                password="test456")

        self.user_one_payment_type = PaymentType.objects.create(user=self.user_one, 
                name="Visa", 
                account_number=1234567890123456)
        self.user_two_payment_type = PaymentType.objects.create(user=self.user_two, 
                name="Mastercard", 
                account_number=987654321098765)

        self.client = Client()
        self.client.force_login(self.user_one)

        self.response = self.client.get(reverse('website:edit_payment_type'))    

    def test_user_payment_type_is_in_response(self):        
        self.assertIn(self.user_one_payment_type, self.response.context['payment_types'])

    def test_other_user_payment_type_is_not_in_response(self):        
        self.assertNotIn(self.user_two_payment_type, self.response.context['payment_types'])

    def test_response_redirects_to_no_payment_type_view_if_no_payment_type(self):
        self.user_one_payment_type.delete()
        response = self.client.get(reverse('website:edit_payment_type'))    
        self.assertRedirects(response, expected_url=reverse('website:no_payment_type'), status_code=302, target_status_code=200)










