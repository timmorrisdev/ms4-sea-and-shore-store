from django.test import TestCase, Client

from django.contrib.auth.models import User

from products.models import Product
from product_reviews.models import ProductReview


class TestProductReviewModels(TestCase):
    '''Test product review model'''

    def test_product_review_model(self):
        '''Test product review model'''

        # initialise user instanse
        test_user = User.objects.create(
            username='testuser',
            email='user@test.com',
            password='usertestpassword'
        )

        # initialise product instance

        test_product = Product.objects.create(
            code='1234',
            name='test_product',
            description='this is a product',
            has_variations=True,
            price=12.34,
            brand='brand',
        )

        # initialise wishlist instance

        test_product_review = ProductReview.objects.create(
            reviewer=test_user,
            product=test_product,
            rating=2,
            title='test review title',
            review='this is a test review'
        )

        self.assertEqual(str(test_product_review), "this is a test review")
