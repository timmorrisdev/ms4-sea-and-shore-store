from django.contrib import admin
from .models import UserWishlist


class UserWishlistAdmin(admin.ModelAdmin):
    '''Admin cofiguration for wishlist model'''
    model = UserWishlist


admin.site.register(UserWishlist, UserWishlistAdmin)
