from django.test import TestCase

from django.urls import reverse, resolve
from wishlist.views import Wishlist, toggle_wishlist


class TestWishlistUrls(TestCase):

    def test_wishlist_url_is_resolved(self):
        url = reverse('wishlist')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Wishlist)
    
    def test_toggle_wishlist_url_is_resolved(self):
        url = reverse('toggle_wishlist', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, toggle_wishlist)
