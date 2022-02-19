from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import ProductReview

from .forms import ProductReviewForm


# def get_product(product_id):
#     ''' get product'''

#     def decorator(*args, **kwargs):
#         def wrapper(*args, **kwargs):
#             print(product_id)
#         return wrapper
#     return decorator

@login_required
# @get_product
def add_product_review(request, product_id):
    """ Add a review and rating to the product """

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. \
                                     Please ensure the form is valid.')
    else:
        form = ProductReviewForm()

    template = 'product_reviews/add_product_review.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def edit_product_review(request, review_id):
    """ Add a review and rating to the product """

    try:
        review = ProductReview.objects.get(pk=review_id)
    except Product.DoesNotExist:
        messages.error(request, 'Review not found.')
        return redirect(reverse('products'))

    try:
        product = Product.objects.get(pk=review.product_id)
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
        return redirect(reverse('products'))

    if review.reviewer == request.user:

        if request.method == 'POST':
            form = ProductReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.reviewer = request.user
                review.product = product
                review.save()
                messages.success(request,
                                 'Successfully updated product review!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed update review. \
                                         Please ensure the form is valid.')
        else:
            form = ProductReviewForm(instance=review)
    else:
        messages.error(request, "Sorry, you don't have permission do that.")
        return redirect(reverse('home'))

    template = 'product_reviews/edit_product_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review
    }

    return render(request, template, context)


@login_required()
def delete_product_review(request, review_id):
    """ Delete review and rating from the product """

    try:
        review = ProductReview.objects.get(pk=review_id)
    except Product.DoesNotExist:
        messages.error(request, 'Review not found.')
        return redirect(reverse('products'))

    try:
        product = Product.objects.get(pk=review.product_id)
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
        return redirect(reverse('products'))

    if review.reviewer == request.user:
        review.delete()

        messages.success(request, 'Successfully deleted product review!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.error(request, "Sorry, you don't have permission do that.")
        return redirect(reverse('home'))
