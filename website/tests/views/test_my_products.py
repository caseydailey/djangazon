from django.test import Client, TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from website.models import Product, Category, Order, UserOrder, PaymentType, Ratings

class TestMyProducts(TestCase):

    def setUp(self):
        self.user_one = User.objects.create(username='test1', password='test123')
        self.user_two = User.objects.create(username='test2', password='test456')
        self.user_three = User.objects.create(username='test3', password='test789')

        self.user_two_payment_type = PaymentType.objects.create(user=self.user_two, name='Visa', account_number=1234567890123456)
        self.user_three_payment_type = PaymentType.objects.create(user=self.user_three, name='Mastercard', account_number=987654321098765)

        self.category = Category.objects.create(category_name='Sports')

        self.product_one = Product.objects.create(
                seller=self.user_one,
                product_category=self.category,
                quantity=3,
                description="Very cool Product1",
                price=20.00,
                date_created="2014-06-05",
                title="Cool product1",
                local_delivery=False,
                city="Nashville")
        self.product_two = Product.objects.create(
              seller=self.user_one,
              product_category=self.category,
              quantity=5,
              description="Very cool Product2",
              price=23.21,
              date_created="2014-06-05",
              title="Cool product2",
              local_delivery=False,
              city="Nashville")

        self.client = Client()
        self.client.force_login(self.user_one)

    def test_status_code_is_200(self): 
        response = self.client.get(reverse('website:my_products'))

        self.assertEqual(response.status_code, 200)  

    def test_sold_products_show_in_response(self):
        user_two_order = Order.objects.create(buyer=self.user_two,
            payment_type=self.user_two_payment_type,
            date_complete='2016-05-06')

        UserOrder.objects.create(product=self.product_one, order=user_two_order)
        UserOrder.objects.create(product=self.product_two, order=user_two_order)

        response = self.client.get(reverse('website:my_products'))

        self.assertEqual(response.context['num_of_products_sold']['Cool product1'], 1)
        self.assertEqual(response.context['num_of_products_sold']['Cool product2'], 1)

    def test_all_users_products_to_sell_in_response(self):
        response = self.client.get(reverse('website:my_products'))

        self.assertIn(self.product_one, response.context['user_products'])
        self.assertIn(self.product_two, response.context['user_products'])

    # def test_average_rating_of_products_sold_in_response(self):
    #     user_two_order = Order.objects.create(buyer=self.user_two,
    #         payment_type=self.user_two_payment_type,
    #         date_complete='2016-05-06')

    #     UserOrder.objects.create(product=self.product_one, order=user_two_order)        

    #     Ratings.objects.create(user=self.user_two,
    #             product=self.product_one,
    #             rating=5)

    #     response = self.client.get(reverse('website:my_products'))

    #     self.assertEqual(response.context['average_rating_for_products']['Cool product1'], 5)

    #     user_three_order = Order.objects.create(buyer=self.user_three,
    #             payment_type=self.user_three_payment_type,
    #             date_complete='2017-05-06')

    #     UserOrder.objects.create(product=self.product_one, order=user_three_order)        

    #     Ratings.objects.create(user=self.user_three,
    #             product=self.product_one,
    #             rating=1)

    #     response = self.client.get(reverse('website:my_products'))
    #     self.assertEqual(response.context['average_rating_for_products']['Cool product1'], 3)














