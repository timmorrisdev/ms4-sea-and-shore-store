from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from products.models import Product

from .forms import ProductReviewForm


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
            messages.success(request, 'Successfully added product review!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductReviewForm()

    template = 'product_reviews/add_product_review.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)
