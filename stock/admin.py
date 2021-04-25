from django.contrib import admin
from .models import Stock, Item

# Register your models here.


class AdminItems(admin.ModelAdmin):
    orderList = (
        'sku',
        'name',
        'country',
        'types',
        'image',
    )

    ordering = ('sku',)


class AdminStock(admin.ModelAdmin):
    orderList = (
        'name',
    )


admin.site.register(Stock, AdminStock)
admin.site.register(Item, AdminItems)

