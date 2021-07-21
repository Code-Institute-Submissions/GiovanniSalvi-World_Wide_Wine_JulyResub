from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class MyAccount(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=15, null=False, blank=True)
    default_country = models.CharField(
        max_length=50, null=False, blank=True)
    default_city = models.CharField(
        max_length=20, null=False, blank=True, default="")
    default_postcode = models.CharField(max_length=10, blank=True, default="")
    default_address = models.CharField(max_length=60, null=False, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_account(sender, instance, created, **kwargs):

    if created:
        MyAccount.objects.create(user=instance)
    instance.myaccount.save()
