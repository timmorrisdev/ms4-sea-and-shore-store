from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from products.models import Product


class UserWishlist(models.Model):
    '''Model to store user wishlist items'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_wishlist(sender, instance, created, **kwargs):
    """
    Create or update the user profile - code based on profiles model
    """
    if created:
        UserWishlist.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userwishlist.save()
