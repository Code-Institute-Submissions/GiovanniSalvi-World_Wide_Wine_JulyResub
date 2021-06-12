from django.db import models
import uuid
from django.db.models import Sum
from django.conf import settings


from myaccount.models import MyAccount
from stock.models import Item

# Create your models here.


class Checkout(models.Model):
    order_number = models.CharField(max_length=50, null=False, editable=False)
    my_account = models.ForeignKey(
        MyAccount, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    country = models.CharField(
        max_length=50, null=False, blank=False)
    city = models.CharField(
        max_length=20, null=False, blank=False, default="")
    postcode = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=60, null=False, blank=False)
    delivery = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    total = models.DecimalField(
        max_digits=15, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=15, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.total = self.checkoutitems.aggregate(
            Sum('items_total'))[
                'items_total__sum'] or 0
        if self.total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery = self.total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery = 0
        self.grand_total = self.total + self.delivery
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class Checkout_items(models.Model):
    checkout = models.ForeignKey(
        Checkout, null=False,
        blank=False, on_delete=models.CASCADE, related_name='checkoutitems'
    )
    item = models.ForeignKey(
        Item, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    items_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        self.items_total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.item.sku} on checkout {self.checkout.order_number}'
