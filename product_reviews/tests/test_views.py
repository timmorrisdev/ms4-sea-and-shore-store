from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from products.models import Product
from product_reviews.models import ProductReview


class TestProductViews(TestCase):
    '''Tests for product review views.py '''

    def setUp(self):

        self.client = Client()

        # initialise user instance
        self.user = User.objects.create_user(
            username='testuser',
            email='user@test.com',
            password='usertestpassword'
        )

        self.not_reviewer = User.objects.create(
            username='wronguser',
            email='wrong@test.com',
            password='wrongpassword'
        )

        # initialise product instance
        self.product = Product.objects.create(
            code='1234',
            name='test_product',
            description='this is a product',
            has_variations=True,
            price=12.34,
            brand='brand',
        )

        # initialise product review instance
        self.review = ProductReview.objects.create(
            reviewer=self.user,
            product=self.product,
            rating=2,
            title='test review title',
            review='test review body',
        )

        # urls
        self.add_product_review_url = reverse('add_product_review', kwargs={'product_id':self.product.id})
        self.edit_product_review_url = reverse('edit_product_review', kwargs={'product_id': self.product.id, 'review_id':self.review.id})
        self.delete_product_review_url = reverse('delete_product_review', kwargs={'product_id': self.product.id, 'review_id':self.review.id})

    def test_add_product_review_get_not_user(self):
        '''test add product review get request no user login'''

        # test response
        response = self.client.get(self.add_product_review_url)
        self.assertEqual(response.status_code, 302)

    def test_add_product_review_get(self):
        '''test add product review get request'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.get(self.add_product_review_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product_reviews/add_product_review.html')

    def test_add_product_review_post_form_valid(self):
        '''test add product review post request form valid'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.post(self.add_product_review_url, {
            'reviewer': self.user,
            'product': self.product,
            'rating': 2,
            'title': 'test review title 2',
            'review': 'test review body 2',
        })

        review = ProductReview.objects.get(title='test review title 2')
        self.assertEqual(review.review, 'test review body 2')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_detail', args=[self.product.id]))

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Successfully added product review!')

    def test_add_product_review_post_form_invalid(self):
        '''test add product review post request form valid'''

        # user login
        self.client.login(username="testuser", password="usertestpassword")

        # test response
        response = self.client.post(self.add_product_review_url, {
            'reviewer': '',
            'product': '',
            'rating': '',
            'title': '',
            'review': '',
        })

        # test messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Failed to add review. \
                                     Please ensure the form is valid.')

    def test_edit_product_review_get_not_user(self):
        '''test edit product review not user get'''

        # test response
        response = self.client.get(self.edit_product_review_url)
        self.assertEqual(response.status_code, 302)


    # def test_edit_product_review_get_user(self):
    #     '''test edit product review = user get'''

    #     # user login
    #     self.client.login(username="testuser", password="usertestpassword")

    #     # test response
    #     response = self.client.get(self.edit_product_review_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('home'))

    #     # test messages
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(len(messages), 1)
    #     self.assertEqual(str(messages[0]), "Sorry, you don't have permission do that.")
