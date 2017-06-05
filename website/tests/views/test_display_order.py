from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from website.models import Product, Category, PaymentType, Order

class TestDisplayOrder(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="test", 
                password="test123")

        self.payment_type = PaymentType.objects.create(user=self.user, 
                name="Visa", 
                account_number=1234567890123456)

        self.category = Category.objects.create(category_name="sports")

        self.product_one = Product.objects.create(
            seller=self.user,
            product_category=self.category,
            quantity=3,
            description="Very cool Product",
            price=20.00,
            date_created="2014-06-05",
            title="Cool product",
            local_delivery=False,
            city="Nashville")

        self.order = Order.objects.create(buyer=self.user, 
                payment_type=self.payment_type, 
                date_complete="2017-06-05")

        self.client = Client()
        self.client.force_login(self.user)

    def test_some_implementation(self):
        response = self.client.get(reverse('website:display_order', args={self.order.pk}))
        self.assertEqual(response.status_code, 200)        
