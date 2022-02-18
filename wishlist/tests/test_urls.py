from django.test import TestCase

from django.urls import reverse, resolve
from wishlist.views import Wishlist, toggle_wishlist


class TestWishlistUrls(TestCase):
    '''Test wishlsit urls
    '''
    def test_wishlist_url_is_resolved(self):
        url = reverse('wishlist')
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Wishlist)

    def test_toggle_wishlist_url_is_resolved(self):
        url = reverse('toggle_wishlist', args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func, toggle_wishlist)
