from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import UserWishlist

# Create your views here.


@login_required
def wishlist(request):
    """ Display the user's wishlsit. """

    wishlist = get_object_or_404(UserWishlist, user=request.user)
    wishlist_items = wishlist.products.all()

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
        'wishlist_items': wishlist_items
    }

    return render(request, template, context)


@login_required
def toggle_wishlist(request, product_id):
    ''' Add or remove product to user wishlist'''

    product = get_object_or_404(Product, pk=product_id)
    wishlist = get_object_or_404(UserWishlist, user=request.user)

    # check if product does not exist in user wishlist
    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request,
                         (f'Successfully added {product.name} to wishlist'))
    else:
        wishlist.products.remove(product)
        messages.success(request,
                         (f'Successfully removed {product.name} '
                          f'from wishlist'))

    return redirect(reverse('products'))
