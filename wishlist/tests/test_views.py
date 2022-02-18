from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Category, Product

class TestWishlistViews(TestCase):
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

        # urls
        self.wishlist_url = reverse('wishlist')
        self.toggle_wishlist_url = reverse('toggle_wishlist', kwargs={'product_id': self.product1.id})

    def test_view_wishlist_unregistered(self):
        '''test view wishlist as unregistered user '''

        # test response
        response = self.client.get(self.wishlist_url)
        self.assertEqual(response.status_code, 302)

    def test_view_wishlist_registered(self):
        '''test view wishlist as registered user '''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.wishlist_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_toggle_wishlist_unregistered(self):
        '''test view wishlist as unregistered user '''

        # test response
        response = self.client.get(self.toggle_wishlist_url)
        self.assertEqual(response.status_code, 302)

    def test_toggle_wishlist_registered(self):
        '''test view wishlist as registered user '''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # ADD TO WISHLIST
        # test response
        response = self.client.get(self.toggle_wishlist_url)
        self.assertEqual(response.status_code, 302)

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Successfully added {self.product1.name} to wishlist')

        # REMOVE FROM WISHLIST
        # test response
        response = self.client.get(self.toggle_wishlist_url)
        self.assertEqual(response.status_code, 302)

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]), f'Successfully removed {self.product1.name} '
                          f'from wishlist')

    def test_toggle_wishlist_no_product_registered(self):
        '''test view wishlist as registered user '''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        product = Product.objects.get(id=self.product1.id)
        product.delete()
        # ADD TO WISHLIST
        # test response
        response = self.client.get(self.toggle_wishlist_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('products'))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Product not found.')
