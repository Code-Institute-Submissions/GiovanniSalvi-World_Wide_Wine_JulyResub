from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import MyAccount
from .forms import AccountForm
# Create your views here.

from checkout.models import Checkout

def myaccount(request):
    myaccount = get_object_or_404(MyAccount, user=request.user)
    
    form = AccountForm(instance=myaccount)
    orders = myaccount.orders.all()

    template = 'myaccount/myaccount.html'
    context = {
        'form': form,
        'orders': orders
    }

    return render(request, template, context)
