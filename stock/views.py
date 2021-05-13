from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Item, Stock, Country
from django.shortcuts import get_object_or_404

# Create your views here.


def view_stock(request):

    item = Item.objects.all()
    query = None
    types = None
    country = None

    if request.GET:
        if 'types' in request.GET:
            types = request.GET['types']

            stock = get_object_or_404(Stock, types=types)
            item = item.filter(stock=stock)

        if 'country' in request.GET:
            country = request.GET['country']

            stock = get_object_or_404(Country, country=country)
            item = item.filter(country=stock)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "error")
                return redirect('stock')

            searching = Q(
                name__icontains=query
                ) | Q(
                types__icontains=query) | Q(
                description__icontains=query
                )

            item = item.filter(searching)

    context = {
        'item': item,
        'base': query,
        'stock': types,
        'country': country,
    }

    return render(request, 'stock/stock.html', context)


def item_details(request, item_id):

    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }
    print(context)
    return render(request, 'stock/item_details.html', context)
