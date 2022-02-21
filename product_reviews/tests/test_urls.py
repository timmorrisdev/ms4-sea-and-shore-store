from django.test import TestCase

from django.urls import reverse, resolve
from product_reviews.views import add_product_review, edit_product_review, delete_product_review


class TestProductReviewUrls(TestCase):
    '''Test product review urls'''

    def test_add_product_review_url_is_resolved(self):
        '''add product review url'''

        url = reverse('add_product_review', kwargs={'product_id': 1})

        self.assertEqual(resolve(url).func, add_product_review)

    def test_edit_product_review_url_is_resolved(self):
        '''edit product review url'''

        url = reverse('edit_product_review', kwargs={'product_id': 1, 'review_id': 1})

        self.assertEqual(resolve(url).func, edit_product_review)

    def test_delete_product_review_url_is_resolved(self):
        '''delete product review url'''

        url = reverse('delete_product_review', kwargs={'product_id': 1, 'review_id': 1})

        self.assertEqual(resolve(url).func, delete_product_review)
