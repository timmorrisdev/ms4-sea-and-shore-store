from django.urls import path
from . import views
from .views import Wishlist


urlpatterns = [
    path('', Wishlist.as_view(), name='wishlist'),
    path('toggle_wishlist/<int:product_id>/',
         views.toggle_wishlist, name='toggle_wishlist'),
]
