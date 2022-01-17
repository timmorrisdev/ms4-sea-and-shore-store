from django.contrib import admin
from .models import Product, Category, ProductVariations


class ProductAdmin(admin.ModelAdmin):
    ''' List display for products in admin page '''
    list_display = (
        'code',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('code',)


class CategoryAdmin(admin.ModelAdmin):
    ''' List display for categories in admin page '''
    list_display = (
        'friendly_name',
        'name',
    )


class ProductVariationsAdmin(admin.ModelAdmin):
    ''' List display for categories in admin page '''
    list_display = (
        'product',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductVariations, ProductVariationsAdmin)
