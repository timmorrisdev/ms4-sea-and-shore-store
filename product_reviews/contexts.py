from .models import ProductReview


def product_reviews(request):
    ''' Function to return product reviews to the context'''

    product_reviews = ProductReview.objects.all()
    for review in product_reviews:
        print(review.product.id)

    context = {
        'product_reviews': product_reviews
    }

    return context
