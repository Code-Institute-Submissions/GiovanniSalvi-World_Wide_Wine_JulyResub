from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Item, Stock
from django.shortcuts import get_object_or_404

# Create your views here.


def view_stock(request):

    item = Item.objects.all()
    query = None
    types = None

    if request.GET:
        if 'types' in request.GET:
            types = request.GET['types']

            stock = get_object_or_404(Stock, types=types)
            item = item.filter(stock=stock)

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


