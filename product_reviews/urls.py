from django.urls import path
from . import views

urlpatterns = [
    path('add_product_review/<int:product_id>/', views.add_product_review,
         name='add_product_review'),
]
