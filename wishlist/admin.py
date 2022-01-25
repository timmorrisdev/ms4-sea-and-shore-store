from django.contrib import admin
from .models import UserWishlist


class UserWishlistAdmin(admin.ModelAdmin):
    model = UserWishlist

    # list_display = (
    #     'user',
    #     'product',
    # )

admin.site.register(UserWishlist, UserWishlistAdmin)
