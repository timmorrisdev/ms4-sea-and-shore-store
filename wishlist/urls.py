from django.urls import path
from . import views


urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('toggle_wishlist/<int:product_id>/<path:path>',
         views.toggle_wishlist, name='toggle_wishlist'),
]
