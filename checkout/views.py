from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from .models import Checkout, Checkout_items
from stock.models import Item
from cart.contexts import cart_contents


import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,                                #taken from Boutique Ado
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


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
            'phone_number': request.POST['phone_number'],
        }
        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            checkout = checkout_form.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            checkout.stripe_pid = pid
            checkout.original_cart = json.dumps(cart)
            bag = cart_contents(request)
            checkout.total = bag['total']
            checkout.delivery = bag['delivery']
            checkout.grand_total = bag['grand_total']
            checkout.save()

            for item_id, item_data in cart.items():
                try:
                    item = get_object_or_404(Item, pk=item_id)
                    if isinstance(item_data, int):
                        cartList = Checkout_items(
                            checkout=checkout,
                            item=item,
                            quantity=item_data
                        )
                                                               
                        cartList.save()
                    else:
                        for quantity in item_data.items():
                            cartList = Checkout_items(
                                checkout=checkout,
                                item=item,
                                quantity=item_data
                            ) 
                            cartList.save()
                            print("cartList", cartList)
                except item.DoesNotExist:
                    messages.error(request, (
                        "One of the products  wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    checkout.delete()
                    return redirect(reverse('shopping_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[checkout.order_number]))
        else:
            messages.error(request, 'There was an error with your form.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "your cart is empty at the moment")
            return redirect(reverse('shopping_cart'))
    
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

def checkout_success(request, order_number):

    cartInfo = request.session.get('cartInfo')
    checkout_details = get_object_or_404(Checkout, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {checkout_details.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'checkout_details': checkout_details,
    }

    return render(request, template, context)


