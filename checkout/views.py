from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from cart.contexts import cart_contents

# Create your views here.

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'address': request.POST['address'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            checkout_form.save()
            for item_id, quantity in cart.items():
                item = get_object_or_404(Item, pk=item_id[0])
                total += quantity * item.price
                shopping_counter = total
                cart_list.append({
                    'item_id': item_id,
                    'item': item,
                    'quantity': quantity
                })
                    

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "your cart is empty at the moment")
        return redirect(reverse('cart'))
    
    bag = cart_contents(request)
    total = bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Public key missing in your enviroment')

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)



