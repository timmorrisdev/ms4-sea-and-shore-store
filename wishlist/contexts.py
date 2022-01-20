from django.shortcuts import get_object_or_404
from .models import UserWishlist


def wishlist_items(request):
    """ Pass current wishlist, or none to context """

    wishlist_items = []
    if request.user.is_authenticated:
        wishlist = get_object_or_404(UserWishlist, user=request.user)
        wishlist_items = wishlist.products.all()

    context = {
        'wishlist_items': wishlist_items
    }

    return context
