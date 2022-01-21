from django.contrib import admin

from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    ''' List display for products in admin page '''
    list_display = (
        'product',
        'rating',
        'reviewer',
    )


admin.site.register(ProductReview, ProductReviewAdmin)
