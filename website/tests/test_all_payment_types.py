from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from website.models import PaymentType

class SpecificPaymentTypeTestCases(TestCase):

    def setUp(self):
        user_one = User.objects.create(username="Test guy", password="test123")
        self.payment_type_one = PaymentType.objects.create(
            user=user_one,
            name="Visa",
            account_number=111111111111)
        self.payment_type_two = PaymentType.objects.create(
            user=user_one,
            name="Amex",
            account_number=222222222222)
        self.payment_type_three = PaymentType.objects.create(
            user=user_one,
            name="Mastercard",
            account_number=333333333333)

        self.client = Client()
        self.client.force_login(user_one)

    def test_correct_payment_type_in_view_response(self):
        """
        Verify that the Payment Types view for a customer has all of the payment types in the request context
        test_all_payment_types.py
        """
        response = self.client.get(reverse('website:edit_payment_type'))
        self.assertEqual(response.status_code, 200)        

        self.assertIn(self.payment_type_one, response.context['payment_types'])
        self.assertIn(self.payment_type_two, response.context['payment_types'])
        self.assertIn(self.payment_type_three, response.context['payment_types'])





