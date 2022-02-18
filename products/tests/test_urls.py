from django.test import TestCase

from django.urls import reverse, resolve

from products.views import (ProductList, ProductDetail, AddProduct, EditProduct,
                    DeleteProduct, AddProductVariation,
                    EditProductVariation, DeleteProductVariation)


class TestProductsUrls(TestCase):
    '''Test products urls'''

    def test_product_list_url_is_resolved(self):
        ''' test url'''
        url = reverse('products')
        self.assertEqual(resolve(url).func.view_class, ProductList)

    def test_product_detail_url_is_resolved(self):
        ''' test url'''
        url = reverse('product_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProductDetail)

    def test_product_add_url_is_resolved(self):
        ''' test url'''
        url = reverse('add_product')
        self.assertEqual(resolve(url).func.view_class, AddProduct)

    def test_product_edit_url_is_resolved(self):
        ''' test url'''
        url = reverse('edit_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditProduct)
    
    def test_product_delete_url_is_resolved(self):
        ''' test url'''
        url = reverse('delete_product', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteProduct)

    def test_product_add_variation_url_is_resolved(self):
        ''' test url'''
        url = reverse('add_product_variation', args=[1])
        self.assertEqual(resolve(url).func.view_class, AddProductVariation)

    def test_product_edit_variation_url_is_resolved(self):
        ''' test url'''
        url = reverse('edit_product_variation', args=[1])
        self.assertEqual(resolve(url).func.view_class, EditProductVariation)

    def test_product_delete_variation_url_is_resolved(self):
        ''' test url'''
        url = reverse('delete_product_variation', args=[1])
        self.assertEqual(resolve(url).func.view_class, DeleteProductVariation)
