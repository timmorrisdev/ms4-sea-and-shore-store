from django.test import TestCase

from django.shortcuts import reverse

# Create your tests here.

# class TestWishlistViews(TestCase):
#     '''Tests for views.py '''

#     def test_wishlist_page_url_exists(self):
#         response = self.client.get('/wishlist/')
#         self.assertEqual(response.status_code, 200)

#     def test_the_wishlist_url_is_accessible_by_name(self):
#         response = self.client.get(reverse('wishlist'))
#         self.assertEqual(response.status_code, 200)

#     def test_wishlist_page_template(self):
#         response = self.client.get(reverse('wishlist'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'wishlist/wishlist.html')
