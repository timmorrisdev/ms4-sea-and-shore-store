from django.shortcuts import get_object_or_404
from .models import UserWishlist


def wishlist_items(request):
    """ Pass current wishlist, or none to context """

    wishlist_items = []
    if request.user.is_authenticated:
        try:
            wishlist = UserWishlist.objects.get(user=request.user)
            wishlist_items = wishlist.products.all()
        except UserWishlist.DoesNotExist:
            wishlist_items = []

    context = {
        'wishlist_items': wishlist_items
    }

    return context
