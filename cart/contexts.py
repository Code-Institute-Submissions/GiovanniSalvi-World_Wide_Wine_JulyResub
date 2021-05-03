from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_list = []
    total = 0
    shopping_counter = 0

    if total > settings.FREEDELIVERY_THRESHOLD:
        delivery = 0
    else:
        delivery = total * Decimal(
            settings.DELIVERY_PERCENTAGE / 1000)

    grand_total = delivery + total

    context = {
        'cart_list': cart_list,
        'total': total,
        'shopping_counter': shopping_counter,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
