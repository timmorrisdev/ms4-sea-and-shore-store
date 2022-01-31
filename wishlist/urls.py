from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views
from .views import Wishlist



urlpatterns = [
    # path('', views.wishlist, name='wishlist'),
    path('', Wishlist.as_view(), name='wishlist'),
    path('toggle_wishlist/<int:product_id>/<path:path>',
         views.toggle_wishlist, name='toggle_wishlist'),
]
