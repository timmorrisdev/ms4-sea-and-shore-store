from .models import Product


def get_brands(request):
    ''' Function to return unique brand entries to template
        for use in navigation'''

    products = Product.objects.all()

    get_brands = []
    for product in products:
        brand = product.brand
        get_brands.append(brand)

    brands = (set(get_brands))

    context = {
        'brands': sorted(brands)
    }

    return context
