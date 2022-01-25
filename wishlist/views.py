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

    # do i need this code?
    try:
        UserWishlist.objects.get(user=request.user)
    except UserWishlist.DoesNotExist:
        messages.info(request,
                         ('Nothing in wishlist'))

    template = 'wishlist/wishlist.html'

    return render(request, template)


@login_required
def toggle_wishlist(request, product_id, path):
    ''' Add or remove product to user wishlist'''
    # current_path = path[:-1]
    # print(path)
    # print(current_path)
    # uri = request.build_absolute_uri(path)
    # print(uri)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
        return redirect(reverse('products'))

    try:
        wishlist = UserWishlist.objects.get(user=request.user)
    except UserWishlist.DoesNotExist:
        wishlist = UserWishlist.objects.create(user=request.user)

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
