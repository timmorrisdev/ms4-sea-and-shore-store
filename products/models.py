from django.db import models


class Category(models.Model):
    ''' Model for product categories '''

    class Meta:
        ''' Model to override default addition of s for plural '''
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        ''' Override default object name return '''
        return self.name

    def get_friendly_name(self):
        ''' Return friendly name of category '''
        return self.friendly_name


class Product(models.Model):
    ''' Model for store products '''

    code = models.CharField(max_length=50,
                            null=True,
                            blank=True)
    name = models.CharField(max_length=120)
    description = models.TextField()
    has_variations = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=120)
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        ''' Override default object name return '''
        return self.name

    class Meta:
        '''class to determine default ordering of products'''
        ordering = ('name',)


class ProductVariationManager(models.Manager):
    '''variation manager to return objects in each category'''

    def sizes(self):
        '''return Product objects with size variations'''
        return super(ProductVariationManager, self).filter(category='size')

    def colours(self):
        '''return Product objects with colour variations'''
        return super(ProductVariationManager, self).filter(category='colour')


# Variable of tuples to define category choices in variation model
VARIATION_CATEGORIES = (
    ('size', 'size'),
    ('colour', 'colour')
)


class ProductVariations(models.Model):
    ''' Model for product variations

        References product object as foreign key.
        Uses ProductVariationMnager to return product
        objects within each catagory.
    '''

    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='variations')
    category = models.CharField(max_length=120, choices=VARIATION_CATEGORIES,
                                default='size')
    name = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)

    objects = ProductVariationManager()

    ''' Override default object name return '''
    def __str__(self):
        return self.name
