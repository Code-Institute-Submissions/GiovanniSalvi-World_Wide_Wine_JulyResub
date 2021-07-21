from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from django.contrib import messages
from .models import Item, Stock, Country
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import StockForm

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

    return render(request, 'stock/item_details.html', context)


def add_item(request):
    if request.method == 'POST':
        form = StockForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect(reverse('item_details', args=[item.id]))
    else:
        form = StockForm()

    template = 'stock/add_item.html'
    context = {
        'form' : form,
    }

    return render(request, template, context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = StockForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse('item_details', args=[item.id]))
    else:
        form = StockForm(instance=item)

    template = 'stock/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user.is_superuser:
        item.delete()

    return redirect(reverse('stock'))
         
