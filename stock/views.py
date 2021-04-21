from django.shortcuts import render

# Create your views here.


def view_stock(request):

    """ A view that renders the contact form page """

    return render(request, 'stock/stock.html')
