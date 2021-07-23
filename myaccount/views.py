from django.shortcuts import render, redirect, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import MyAccount
from .forms import AccountForm

from checkout.models import Checkout

def myaccount(request):
    myaccount = get_object_or_404(MyAccount, user=request.user)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=myaccount)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated')
    
    form = AccountForm(instance=myaccount)
    order = myaccount.order.all()

    template = 'myaccount/myaccount.html'
    context = {
        'form': form,
        'order': order,
        'on_myaccount_page': True
    }

    return render(request, template, context)

def shopping_history(request, order_number):
    orders = get_object_or_404(Checkout, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'orders':orders,
        'from_myaccount': True,
    }

    return render(request, template, context)

def remove_order(request, order_number):
    order = get_object_or_404(Checkout, order_number=order_number) 
    order.delete()
    messages.success(request, f'Removed {order_number} from your shopping history')

    return redirect(reverse('myaccount'))
