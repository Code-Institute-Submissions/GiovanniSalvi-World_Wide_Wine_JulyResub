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
    }

    return render(request, template, context)
