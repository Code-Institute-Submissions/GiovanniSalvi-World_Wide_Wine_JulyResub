from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from stock.models import Item


def cart_contents(request):

    cart_list = []
    total = 0
    shopping_counter = 0
    cart = request.session.get('cart', {})

    for item_id, in cart.items():
        item = get_object_or_404(Item, pk=item_id)
        total = item.price
        shopping_counter = total
        cart_list.append({
            'item_id': item_id,
            'item': item
        })

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
