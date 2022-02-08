from django.urls import path
from . import views
from .views import (ProductList, ProductDetail, AddProduct, EditProduct,
                    DeleteProduct, AddProductVariation, 
                    EditProductVariation, DeleteProductVariation)

urlpatterns = [
    # path('', views.all_products, name='products'),
    # path('<int:product_id>/', views.product_detail, name='product_detail'),
    # path('add/', views.add_product, name='add_product'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    # path('add_product_variation/<int:product_id>/', views.add_product_variation, name='add_product_variation'),
    # path('delete_variation/<int:variation_id>/', views.delete_product_variation, name='delete_product_variation'),
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),    
    path('add/', AddProduct.as_view(), name='add_product'),    
    path('edit/<int:pk>/', EditProduct.as_view(), name='edit_product'),
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('add_product_variation/<product_id>/', AddProductVariation.as_view(), name='add_product_variation'),
    path('edit_product_variation/<int:pk>/', EditProductVariation.as_view(), name='edit_product_variation'),
    path('delete_variation/<int:pk>/', DeleteProductVariation.as_view(), name='delete_product_variation'),
]