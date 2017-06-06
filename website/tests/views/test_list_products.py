from django.test import LiveServerTestCase, Client
from django.contrib.auth.models import User
from django.test import RequestFactory
from selenium import webdriver

from website.models import Product, Category

import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8000'

class MySeleniumTests(LiveServerTestCase):    

    @classmethod
    def setUpClass(cls):
        cls.selenium = webdriver.Chrome()        
        cls.factory = RequestFactory()           
        super(MySeleniumTests, cls).setUpClass()        

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):     

        self.selenium.get('{}{}'.format(self.live_server_url, '/register'))

        username_input = self.selenium.find_element_by_name("username")
        password_input = self.selenium.find_element_by_name("password")
        email_input = self.selenium.find_element_by_name("email")
        first_name_input = self.selenium.find_element_by_name("first_name")
        last_name_input = self.selenium.find_element_by_name("last_name")
        phone_number_input = self.selenium.find_element_by_name("phone_number")
        address_input = self.selenium.find_element_by_name("address")

        username_input.send_keys('test')
        password_input.send_keys('test123')
        email_input.send_keys('test@gmail.com')
        first_name_input.send_keys('test')
        last_name_input.send_keys('test')
        phone_number_input.send_keys('6152222222')
        address_input.send_keys('some address')

        self.selenium.find_element_by_xpath('//input[@value="Register"]').click()

        user = User.objects.get(username='test')

        self.client = Client()
        self.client.force_login(user)

        category = Category.objects.create(category_name="test")

        self.product_one = Product.objects.create(
            seller=user,
            product_category=category,
            quantity=3,
            description="Prada",
            price=20.00,
            date_created="2014-06-05",
            title="Test1",
            local_delivery=False,
            city="Test")
        self.product_two = Product.objects.create(
            seller=user,
            product_category=category,
            quantity=5,
            description="Test",
            price=23.21,
            date_created="2014-06-05",
            title="Prada",
            local_delivery=False,
            city="Test")
        self.product_three = Product.objects.create(
            seller=user,
            product_category=category,
            quantity=5,
            description="Test",
            price=23.21,
            date_created="2014-06-05",
            title="Test3",
            local_delivery=False,
            city="Prada")        

        self.selenium.implicitly_wait(3)
        self.selenium.get('{}{}'.format(self.live_server_url, '/'))
        self.selenium.implicitly_wait(3)

        search_input = self.selenium.find_element_by_name("search_box")

        self.selenium.implicitly_wait(3)
        search_input.send_keys('Prada')
        self.selenium.find_element_by_id('search_submit').click()
        self.selenium.implicitly_wait(3) 

        self.assertTrue(self.selenium.find_element_by_xpath('//*[contains(text(), "Test1")]'))            
        self.assertTrue(self.selenium.find_element_by_xpath('//*[contains(text(), "Prada")]'))            
        self.assertTrue(self.selenium.find_element_by_xpath('//*[contains(text(), "Test3")]'))                    

