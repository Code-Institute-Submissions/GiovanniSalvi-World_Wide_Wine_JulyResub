from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MyAccount(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=15, null=False, blank=True)
    default_country = models.CharField(
        max_length=50, null=False, blank=True)
    default_city = models.CharField(
        max_length=20, null=False, blank=False, default="")
    default_postcode = models.CharField(max_length=10, null=True, blank=True)
    default_address = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.user.username
