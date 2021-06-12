from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Checkout_items


@receiver(post_save, sender=Checkout_items)
def update_save_checkout(sender, instance, created, **kwargs):

    instance.checkout.update_total()


@receiver(post_delete, sender=Checkout_items)
def delete_save_checkout(sender, instance, **kwargs):
    
    instance.checkout.update_total()
