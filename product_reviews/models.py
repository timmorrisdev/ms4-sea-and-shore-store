from django.db import models

from django.contrib.auth.models import User
from products.models import Product


class ProductReview(models.Model):
    ''' Model for product review and rating'''

    reviewer = models.ForeignKey(User,
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=1, decimal_places=0,
                                 null=True, blank=True)
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.review
