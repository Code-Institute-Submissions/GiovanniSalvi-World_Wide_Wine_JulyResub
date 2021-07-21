from django.contrib import admin
from .models import Checkout, Checkout_items


class Checkout_itemsAdminInline(admin.TabularInline):
    model = Checkout_items
    readonly_fields = ('items_total',)


class CheckoutAdmin(admin.ModelAdmin):
    inlines = (Checkout_itemsAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery', 'total',
                       'grand_total',)

    fields = ('order_number', 'first_name', 'last_name',
              'email', 'date', 'phone_number', 'country',
              'postcode', 'city', 'address',
              'delivery', 'total', 'grand_total',)

    Checklist = ('order_number', 'date', 'first_name', 'last_name',
                 'delivery', 'total',
                 'grand_total')


admin.site.register(Checkout, CheckoutAdmin)
