from django.test import TestCase, Client

from django.contrib.auth.models import User

from wishlist.models import UserWishlist



class TestWishlistModels(TestCase):
    '''Test wishlist model'''

    def test_wishlist_model(self):
        '''Test wishlist model'''

        # initialise user instanse
        test_user = User.objects.create(
            username='testuser',
            email='user@test.com',
            password='usertestpassword'
        )

        # initialise wishlist instance

        test_wishlist = UserWishlist.objects.create(
            user=test_user,
        )

        self.assertEqual(str(test_wishlist), "testuser")
