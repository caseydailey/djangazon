from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from website.models import Product, Category

class TestIndex(TestCase):

    def setUp(self):

        user = User.objects.create(username="test", password="test123")

        category = Category.objects.create(category_name="Sports")

        self.product_one = Product.objects.create(
            seller=user,
            product_category=category,
            quantity=3,
            description="Very cool Product1",
            price=20.00,
            date_created="2014-06-05",
            title="Cool product1",
            local_delivery=False,
            city="Nashville")

        self.response = Client().get(reverse('website:index'))    

    def test_response_code_is_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_latest_product_in_index_response(self):
        self.assertIn(self.product_one, self.response.context['newest_20_products'])
