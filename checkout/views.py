from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CheckoutForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "your cart is empty at the moment")
        return redirect(reverse('cart'))

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_51Iz7f1H57YJj3Apn2JCxj7EJct7OO7REbKQF24VyDXpHcV7XeDbnzHxLh6bzAXURKSpjxB26cd8FwsVEqjwtetpX003FixkFST',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
