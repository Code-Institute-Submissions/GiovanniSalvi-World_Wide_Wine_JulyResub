from django.shortcuts import render
from .models import Item
# Create your views here.


def view_stock(request):

    """ A view that renders the contact form page """

    item = Item.objects.all()

    context = {
        'item': item,
    }

    return render(request, 'stock/stock.html', context)
