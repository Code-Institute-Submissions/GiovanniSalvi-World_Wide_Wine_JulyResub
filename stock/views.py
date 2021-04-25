from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Item

# Create your views here.


def view_stock(request):

    item = Item.objects.all()
    query = None
    types = None
    # country = None#

    if request.GET:
        if 'item' in request.GET:
            types = request.GET['types']
            # country = request.GET['country']#
            item = item.filter(item__types__in=types)

            # item = item.filter(item__country__in=country)#

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "error")
                return redirect('stock')

            searching = Q(
                name__icontains=query
                ) | Q(
                country__icontains=query) | Q(
                description__icontains=query
                )

            item = item.filter(searching)

    context = {
        'item': item,
        'base': query,
        'stock': types,
    }

    return render(request, 'stock/stock.html', context)
