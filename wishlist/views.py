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
def toggle_wishlist(request, product_id, path):
    ''' Add or remove product to user wishlist'''
    current_path = path[:-1]
    print(path)
    print(current_path)

    uri = request.build_absolute_uri(path)
    print(uri)

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

    template = f'https://8000-tan-puma-6qrvi9ci.ws-eu28.gitpod.io/{path}'

    return redirect(template)
    # return redirect(uri)
