from django.urls import path
from .views import (ProductList, ProductDetail, AddProduct, EditProduct,
                    DeleteProduct, AddProductVariation,
                    EditProductVariation, DeleteProductVariation)

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>/',
         ProductDetail.as_view(), name='product_detail'),
    path('add/',
         AddProduct.as_view(), name='add_product'),
    path('edit/<int:pk>/',
         EditProduct.as_view(), name='edit_product'),
    path('delete/<int:pk>/',
         DeleteProduct.as_view(), name='delete_product'),
    path('add_product_variation/<product_id>/',
         AddProductVariation.as_view(), name='add_product_variation'),
    path('edit_product_variation/<int:pk>/',
         EditProductVariation.as_view(), name='edit_product_variation'),
    path('delete_variation/<int:pk>/',
         DeleteProductVariation.as_view(), name='delete_product_variation'),
]
