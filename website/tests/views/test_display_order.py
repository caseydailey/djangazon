from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from decimal import *

from website.models import Product, Category, PaymentType, Order, UserOrder

class TestDisplayOrder(TestCase):

    def setUp(self):
        user = User.objects.create(username="test", 
                password="test123")

        payment_type = PaymentType.objects.create(user=user, 
                name="Visa", 
                account_number=1234567890123456)

        category = Category.objects.create(category_name="sports")

        product_one = Product.objects.create(
            seller=user,
            product_category=category,
            quantity=3,
            description="Very cool Product1",
            price=20.00,
            date_created="2014-06-05",
            title="Cool product1",
            local_delivery=False,
            city="Nashville")
        product_two = Product.objects.create(
            seller=user,
            product_category=category,
            quantity=5,
            description="Very cool Product2",
            price=23.21,
            date_created="2014-06-05",
            title="Cool product2",
            local_delivery=False,
            city="Nashville")

        self.order = Order.objects.create(buyer=user, 
                payment_type=payment_type, 
                date_complete="2017-06-05")

        self.user_order_one = UserOrder.objects.create(product=product_one, order=self.order)
        self.user_order_two = UserOrder.objects.create(product=product_two, order=self.order)

        client = Client()
        client.force_login(user)

        self.response = client.get(reverse('website:display_order', args={self.order.pk}))

    def test_response_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)        

    def test_target_order_is_in_response(self):
        self.assertEqual(self.response.context['target_order'], self.order)

    def test_all_products_is_in_response(self):
        self.assertIn(self.user_order_one, self.response.context['all_products'])
        self.assertIn(self.user_order_two, self.response.context['all_products'])

    def test_total_of_products_in_order_is_in_response(self):
        self.assertEqual(self.response.context['total'], Decimal('43.21'))










