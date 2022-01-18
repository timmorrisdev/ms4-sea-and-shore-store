from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserWishlist
from products.models import Product

# Create your views here.


@login_required
def wishlist(request):
    """ Display the user's wishlsit. """
    wishlist = get_object_or_404(UserWishlist, user=request.user)

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist
    }

    return render(request, template, context)


# def wishlist(request):
#     """
#     A view to render the users wishlist
#     """
#     wishlist = None
#     try:
#         wishlist = WishList.objects.get(user=request.user)
#     except WishList.DoesNotExist:
#         pass

#     context = {
#         'wishlist': wishlist,
#     }

#     return render(request, 'wishlist/wishlist.html', context=context)

def add_to_wishlist(request, product_id):
    print('wishlist add')
    product = get_object_or_404(Product, pk=product_id)
    wishlist = get_object_or_404(UserWishlist, user=request.user)

    print(wishlist.products)

    if product not in wishlist.products.all():
        # print('if')
        wishlist.products.add(product)
        print('added')
        print(wishlist.products)
        messages.success(request, 'Product successfully added to wishlist')
    else:
        wishlist.products.remove(product)
        print('removed')
        print(wishlist.products)
        messages.success(request, 'Product successfully removed from wishlist')



    
    context = {

    }

    return redirect(reverse('products'))


# messages.error(request, "Update failed, please ensure form is valid")