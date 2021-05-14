from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from stock.models import Item

# Create your views here.


def shopping_cart(request):
    return render(request, 'cart/cart.html')


def add_shopping(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))

    if item_id in list(cart.keys()):
        cart[item_id[0]] += quantity
    else:
        cart[item_id[0]] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity'))
    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def remove_cart(request, item_id):
    cart = request.session.get('cart', {})
    item = get_object_or_404(Item, pk=item_id)
    cart.pop(item_id)
    messages.success(request, f'Removed {item.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))
