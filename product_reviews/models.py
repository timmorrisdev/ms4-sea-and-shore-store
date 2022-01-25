from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
from products.models import Product


class ProductReview(models.Model):
    ''' Model for product review and rating'''

    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
                                 MinValueValidator(1),
                                 MaxValueValidator(5)],
                                 default=1, null=False, blank=False)
    title = models.CharField(max_length=150, default="Product Review")
    review = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
