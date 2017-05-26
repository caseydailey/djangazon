from django.test import Client, TestCase
from django.urls import reverse
from website.models import User, PaymentType
# * Verify that the Payment Types view for a customer has all of the payment types in the request context

class SpecificPaymentTypeTestCases(TestCase):

    def setUp(self):
        user_one = User.objects.create( name="Test payment guy", password="test123")
        self.payment_type_one = PaymentType.objects.create(name="visa")
        self.payment_type_two = PaymentType.objects.create(name="amex")
        self.payment_type_three = PaymentType.objects.create(name="mastercard")

        self.payment_type_one = PaymentType.objects.create(
                user=user_one,
                name=self.payment_type_one,
                account_number=111111111111)

        self.payment_type_two = PaymentType.objects.create(
            user=user_one,
            name=self.payment_type_one,
            account_number=222222222222)

        self.payment_type_three = PaymentType.objects.create(
            user=user_one,
            name=self.payment_type_one,
            account_number=333333333333)

        client = Client()
        client.login(
            username="Test payment guy",
            password="test123"
        )

    def test_correct_payment_type_in_view_response(self):
        response = self.client.get(reverse('website:edit_payment_type', arg={self.payment_type_one.pk}))
        self.assertContains(response.context['visa'], self.payment_type_one)
        self.assertContains(response.context['amex'], self.payment_type_two)
        self.assertContains(response.context['mastercard'], self.payment_type_three)
        self.assertEqual(response.context['visa'], self.payment_type_one)
        self.assertEqual(response.context['amex'], self.payment_type_two)
        self.assertEqual(response.context['mastercard'], self.payment_type_three)



                        

