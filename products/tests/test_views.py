from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Category, Product, ProductVariations

import json

class TestProductViews(TestCase):
    '''Tests for views.py '''

    # fixtures = [
    #     'category.json',
    #     'products.json',
    #     'product_variations.json'
    # ]

    def setUp(self):

        self.client = Client()

        # initialise user instance
        self.user = User.objects.create_user(
            username='testuser',
            email='user@test.com',
            password='usertestpassword'
        )

        # initialise superuser instance
        self.super_user = User.objects.create_superuser(
            username='testsuper',
            email='super@test.com',
            password='supertestpassword'
        )

        # initialise category instanse
        self.category1 = Category.objects.create(
            name='test_category1',
            friendly_name='category1'
        )

        # initialise product instance
        self.product1 = Product.objects.create(
            code='1234',
            name='test_product',
            description='this is a product',
            has_variations=True,
            price=12.34,
            brand='brand',
            category=self.category1
        )

        # initialise product variation instance
        self.product_variation1 = ProductVariations.objects.create(
            product=self.product1,
            category='size',
            name='variation1'
        )

        # print(self.product1.category)

        # urls
        self.products_url = reverse('products')
        self.detail_url = reverse('product_detail', args=[self.product1.pk])
        self.add_product_url = reverse('add_product')
        self.edit_product_url = reverse('edit_product', args=[self.product1.pk])
        self.delete_product_url = reverse('delete_product', args=[self.product1.pk])
        self.add_product_variation_url = reverse('add_product_variation', args=[self.product1.pk])
        self.edit_product_variation_url = reverse('edit_product_variation', args=[self.product_variation1.pk])
        self.delete_product_variation_url = reverse('delete_product_variation', args=[self.product_variation1.pk])

    def test_product_list_get(self):
        '''test get all products'''

        # test response
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_get(self):
        '''test product detail get request'''

        # test response
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_get_not_superuser(self):
        '''test add product get request'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sorry, only store owners can do that.')

    def test_add_product_get_superuser(self):
        '''test add product get request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_post_form_valid(self):
        '''test add product post request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.add_product_url, {
            'name': 'test_product2',
            'description': 'this is a product2',
            'has_variations': False,
            'price': 12.34,
            'brand': 'brand',
        })

        product = Product.objects.get(name='test_product2')
        self.assertEqual(product.name, 'test_product2')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_detail', args=(product.id,)))

    def test_add_product_with_variations_post_form_valid(self):
        '''test add product post request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.add_product_url, {
            'name': 'test_product2',
            'description': 'this is a product2',
            'has_variations': True,
            'price': 12.34,
            'brand': 'brand',
        })

        product = Product.objects.get(name='test_product2')
        self.assertEqual(product.name, 'test_product2')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('add_product_variation', args=(product.id,)))
    
    def test_add_product_post_form_invalid(self):
        '''test add product post request form invalid'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.add_product_url, {
            'name': '',
            'description': '',
            'price': '',
            'brand': 'brand',
        })

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to add product. \
                                      Please ensure the form is valid.')

    def test_edit_product_get_not_superuser(self):
        '''test edit product get'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.edit_product_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sorry, only store owners can do that.')

    def test_edit_product_get_superuser(self):
        '''test edit product get'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.get(self.edit_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'You are editing {self.product1.name}')

    def test_delete_product_get_not_superuser(self):
        '''test delete product not superuser'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.delete_product_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sorry, only store owners can do that.')

    def test_delete_product_get_superuser(self):
        '''test delete product superuser'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.get(self.delete_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/delete_product.html')

    def test_add_product_variation_get_not_superuser(self):
        '''test add product variation not superuser'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.add_product_variation_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sorry, only store owners can do that.')

    def test_add_product_variation_get_superuser(self):
        '''test add product variation superuser'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.get(self.add_product_variation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product_variation.html')

    def test_edit_product_variation_get_not_superuser(self):
        '''test edit product variation not superuser'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.edit_product_variation_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sorry, only store owners can do that.')

    def test_edit_product_variation_get_superuser(self):
        '''test edit product variation superuser'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.get(self.edit_product_variation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product_variation.html')

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'You are editing variation \
                                    {self.product_variation1.name} on \
                                    {self.product_variation1.product.name}')
        
    def test_delete_product_variation_get_not_superuser(self):
        '''test delete product variation not superuser'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.delete_product_variation_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Sorry, only store owners can do that.')
    
    def test_delete_product_variation_get_superuser(self):
        '''test delete product variation superuser'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.get(self.delete_product_variation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/delete_product_variation.html')



# message = str(messages[0])
# print(message)