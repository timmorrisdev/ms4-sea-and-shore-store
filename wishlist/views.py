from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from django.http import HttpResponseRedirect


from products.models import Product
from .models import UserWishlist


@method_decorator(login_required, name='dispatch')
class Wishlist(View):
    """ Display the user's wishlsit. """

    def get(self, request):

        template_name = 'wishlist/wishlist.html'

        return render(request, template_name)


# @login_required
# def wishlist(request):
#     """ Display the user's wishlsit. """

#     template = 'wishlist/wishlist.html'

#     return render(request, template)


@login_required
def toggle_wishlist(request, product_id, path):
    ''' Add or remove product to user wishlist'''

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

    if len(wishlist.products.all()) < 1:
        wishlist.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
