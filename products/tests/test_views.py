from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Category, Product, ProductVariations


class TestProductViews(TestCase):
    '''Tests for views.py '''

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

        # urls
        self.products_url = reverse('products')
        self.detail_url = reverse('product_detail', args=[self.product1.id])
        self.add_product_url = reverse('add_product')
        self.edit_product_url = reverse('edit_product', args=[self.product1.id])
        self.delete_product_url = reverse('delete_product', args=[self.product1.id])
        self.add_product_variation_url = reverse('add_product_variation', kwargs={'product_id': self.product1.id})
        self.edit_product_variation_url = reverse('edit_product_variation', args=[self.product_variation1.id])
        self.delete_product_variation_url = reverse('delete_product_variation', args=[self.product_variation1.id])

    def test_product_list_get(self):
        '''test get all products'''

        # test response
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_list_with_query_get(self):
        ''' Test get all products with search '''

        response = self.client.get(self.products_url, {'q': 'test_query'})
        context = response.context
        self.assertTrue(context['search_term'])
        self.assertEqual(context['search_term'], 'test_query')

    def test_product_list_with_blank_query_get(self):
        ''' Test get all products with no search term '''

        response = self.client.get(self.products_url, {'q': ''})

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You didn't enter any search criteria!")

    def test_product_list_with_category_get(self):
        ''' Test get all products with category '''

        response = self.client.get(self.products_url, {'category': 'test_category'})
        context = response.context
        self.assertTrue(context['current_category'])
        self.assertEqual(context['current_category'], 'test_category')

    def test_product_list_with_sort_get(self):
        ''' Test get all products with sorting '''

        response = self.client.get(self.products_url, {'sort': 'name'})
        context = response.context
        self.assertTrue(context['current_sorting'])
        self.assertEqual(context['current_sorting'], 'name')

    def test_product_list_with_direction_get(self):
        ''' Test get all products with direction '''

        response = self.client.get(self.products_url, {'sort': 'name', 'direction': 'desc'})
        context = response.context
        self.assertTrue(context['current_sorting'])
        self.assertEqual(context['current_sorting'], '-name')

    def test_product_list_with_brand_get(self):
        ''' Test get all products with brand '''

        response = self.client.get(self.products_url, {'brand': 'vans'})
        context = response.context
        queryset = Product.objects.filter(brand__icontains='vans')

        self.assertQuerysetEqual(context['object_list'], map(repr, queryset))

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

        # test initial form data matches
        self.assertEqual(response.context['form'].initial['name'], self.product1.name)
        self.assertEqual(response.context['form'].initial['brand'], self.product1.brand)          

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'You are editing {self.product1.name}')
    
    def test_edit_product_post_form_valid(self):
        '''test add product post request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.edit_product_url, {
            'name': 'test_product2',
            'description': 'edited description',
            'has_variations': True,
            'price': 12.34,
            'brand': 'edited brand',
        })

        # test updated product fields
        product = Product.objects.get(id=self.product1.id)
        self.assertEqual(product.description, 'edited description')
        self.assertEqual(product.brand, 'edited brand')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_detail', args=(product.id,)))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully updated product!')

    def test_edit_product_post_form_invalid(self):
        '''test edit product post request form invalid'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.edit_product_url, {
            'name': '',
            'description': '',
            'price': '',
            'brand': 'brand',
        })

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to edit product. \
                                      Please ensure the form is valid.')

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
    
    def test_delete_product_post_superuser(self):
        '''test delete product superuser'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.delete_product_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully deleted product!')

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

    def test_add_product_variation_post_form_valid(self):
        '''test add product variation post request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.add_product_variation_url, {
            'name': 'test_variation',
            'product': self.product1,
            'category': 'size'
        })

        variation = ProductVariations.objects.get(name='test_variation')
        self.assertEqual(variation.category, 'size')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('add_product_variation', args=(self.product1.id,)))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully added product variation!')

    def test_add_product_variation_post_form_invalid(self):
        '''test add product variation post request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.add_product_variation_url, {
            'name': '',
            'product': '',
            'category': '',
        })

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to add product. \
                                      Please ensure the form is valid.')

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

    def test_edit_product_variation_post_form_valid(self):
        '''test add product post request'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.edit_product_variation_url, {
            'name': 'edited_variation',
            'product': self.product1,
            'category': 'size'
        })

        # test updated product fields
        variation = ProductVariations.objects.get(id=self.product_variation1.id)
        self.assertEqual(variation.name, 'edited_variation')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('add_product_variation', args=(variation.product.id,)))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully updated product variation!')

    def test_edit_product_variation_post_form_invalid(self):
        '''test edit product post request form invalid'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.edit_product_variation_url, {
            'name': '',
            'product': '',
            'category': ''
        })

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to update product variation. \
                                      Please ensure the form is valid.')

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

    def test_delete_product_post_superuser(self):
        '''test delete product superuser'''

        # superuser login
        self.client.login(username="testsuper", password="supertestpassword")

        # test response
        response = self.client.post(self.delete_product_variation_url)
        self.assertRedirects(response, reverse('add_product_variation', args=[self.product1.id]))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully deleted product variation!')


# message = str(messages[0])
# print(message)