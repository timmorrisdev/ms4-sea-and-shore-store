from django import template
from product_reviews.models import ProductReview


register = template.Library()


@register.filter(name='review_count')
def review_count(product_id):
    reviews = ProductReview.objects.all()
    product_reviews = 0

    for review in reviews:
        if product_id == review.product.id:
            product_reviews += 1

    return product_reviews
