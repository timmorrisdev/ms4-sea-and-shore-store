from django.test import TestCase, Client

from products.models import Category, Product, ProductVariations


class TestProductModels(TestCase):
        
    def test_category_model(self):
        # initialise category instanse
        test_category = Category.objects.create(
            name='test_category',
            friendly_name='category'
        )

        self.assertEqual(str(test_category), "test_category")
    
    def test_product_model(self):

        test_category = Category.objects.create(
            name='test_category',
            friendly_name='category'
        )

        # initialise product instance
        test_product = Product.objects.create(
            code='1234',
            name='test_product',
            description='this is a product',
            has_variations=True,
            price=12.34,
            brand='brand',
            category=test_category
        )

        self.assertEqual(str(test_product), "test_product")

    def test_product_variation_model(self):

        test_category = Category.objects.create(
            name='test_category',
            friendly_name='category'
        )

        # initialise product instance
        test_product = Product.objects.create(
            code='1234',
            name='test_product',
            description='this is a product',
            has_variations=True,
            price=12.34,
            brand='brand',
            category=test_category
        )

        # initialise product variation instance
        test_product_variation = ProductVariations.objects.create(
            product=test_product,
            category='size',
            name='test_variation'
        )

        self.assertEqual(str(test_product_variation), "test_variation")