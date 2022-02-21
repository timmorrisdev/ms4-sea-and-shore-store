from django.shortcuts import redirect, reverse

from django.contrib import messages

from products.models import Product
from product_reviews.models import ProductReview


def authenticate_product(func):
    ''' get product'''
    def wrapper(request, *args, **kwargs):
        print('in product decorator')
        print(kwargs)
        '''Check if product exists before returning to function'''
        try:
            # return function if exists
            product = Product.objects.get(pk=kwargs['product_id'])
            print('product found')
            return func(request, *args, **kwargs)
        except Product.DoesNotExist:
            # redirect if product not found
            print('product not found')
            messages.error(request, 'Product not found.')
            return redirect(reverse('products'))

    return wrapper


def authenticate_review(func):
    ''' get review and reviewer'''
    def wrapper(request, *args, **kwargs):
        '''Check if review exists and authentiacate reviewer'''
        print('in review decorator')
        print(kwargs)
        # get review
        try:
            review = ProductReview.objects.get(pk=kwargs['review_id'])
            print('review found')
            # return func(request, *args, **kwargs)
        except Product.DoesNotExist:
            print('review not found')
            messages.error(request, 'Review not found.')
            return redirect(reverse('products'))

        # check user is equal to reviewer
        if review.reviewer == request.user:
            print('reviewer authenticated')
            return func(request, *args, **kwargs)
        else:
            messages.error(request, "Sorry, you don't have permission do that.")
            return redirect(reverse('home'))

    return wrapper
