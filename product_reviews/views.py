from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import ProductReview

from .forms import ProductReviewForm


@login_required
def add_product_review(request, product_id):
    """ Add a review and rating to the product """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            update_product_rating(product)
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
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

    review = get_object_or_404(ProductReview, pk=review_id)
    product = get_object_or_404(Product, pk=review.product.id)
    product_id = review.product.id
    print(product_id)

    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            update_product_rating(product)
            messages.success(request, 'Successfully updated product review!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed update review. Please ensure the form is valid.')
    else:
        form = ProductReviewForm(instance=review)


    template = 'product_reviews/edit_product_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review
    }

    return render(request, template, context)


@login_required()
def delete_product_review(request, review_id):

    review = get_object_or_404(ProductReview, pk=review_id)
    product = get_object_or_404(Product, pk=review.product.id)
    product_id = review.product.id
    review.delete()

    messages.success(request, 'Successfully deleted product review!')
    return redirect(reverse('product_detail', args=[product_id]))



def update_product_rating(product):
    '''update product rating'''

    reviews = ProductReview.objects.all()
    product_reviews = reviews.filter(product=product)

    total = 0
    for i in product_reviews:
        total += i.rating

    new_rating = round(total / len(product_reviews), 2)
    product.rating = new_rating
    product.save()
