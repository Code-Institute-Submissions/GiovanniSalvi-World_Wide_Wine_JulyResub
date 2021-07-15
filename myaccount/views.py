from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import MyAccount
from .forms import AccountForm
# Create your views here.

from checkout.models import Checkout

def myaccount(request):
    myaccount = get_object_or_404(MyAccount, user=request.user)

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=myaccount)
        if form.is_valid():
            form.save()
    
    form = AccountForm(instance=myaccount)
    #order = myaccount.orders.all()

    template = 'myaccount/myaccount.html'
    context = {
        'form': form,
        #'order': order,
    }

    return render(request, template, context)
