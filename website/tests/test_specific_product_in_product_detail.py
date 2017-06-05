from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from website.models import Category, Product


class SpecificCategoryTestCases(TestCase):

    def setUp(self):
        user = User.objects.create(username="Test guy", password="test123")        
        self.category = Category.objects.create(category_name="electronics")

        self.product = Product.objects.create(
            seller=user,
            product_category=self.category,
            quantity=2, 
            description="Something electronic", 
            price=350.00, 
            date_created="2014-12-12", 
            title="Computer")        

        client = Client()
        client.login(
            username="Test guy",
            password="test123"
        )

    def test_product_is_created_and_shows_in_product_detail_view_response(self):
        """
        Verify that when a product is created that the Product Detail view has the correct product in the response context
        test_specific_product_in_product_detail.py
        """
        response = self.client.get(reverse('website:product_details', args={self.product.pk}))        
        self.assertEqual(self.product, response.context['product'])        

    def test_product_attributes_show_in_product_details_view_body(self):
        """
        Verify that when a product is created that the Product Detail view has the title, description, price and quantity are in the response body
        test_specific_product_in_product_detail.py
        """
        response = self.client.get(reverse('website:product_details', args={self.product.pk}))
        self.assertContains(response, "Computer")
        self.assertContains(response, "Something electronic")
        self.assertContains(response, 350.00)
        self.assertContains(response, 2)




