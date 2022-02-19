from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from product_reviews.models import ProductReview


@receiver(post_save, sender=ProductReview)
def update_on_save(sender, instance, **kwargs):
    '''Update product rating on review save'''

    reviews = ProductReview.objects.filter(product=instance.product)

    new_rating = 1

    if reviews:
        total = 0
        for i in reviews:
            total += i.rating

        new_rating = round(total / len(reviews), 2)

    instance.product.update_product_rating(new_rating)


@receiver(post_delete, sender=ProductReview)
def update_on_delete(sender, instance, **kwargs):
    '''Update product rating on review delete'''

    reviews = ProductReview.objects.filter(product=instance.product)

    new_rating = 1

    if reviews:
        total = 0
        for i in reviews:
            total += i.rating

        new_rating = round(total / len(reviews), 2)

    instance.product.update_product_rating(new_rating)
