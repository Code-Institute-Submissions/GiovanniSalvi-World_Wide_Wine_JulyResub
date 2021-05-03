from django.shortcuts import render, redirect

# Create your views here.


def shopping_cart(request):

    return render(request, 'cart/cart.html')


def add_shopping(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    request.session['cart'] = cart
    return redirect(redirect_url)
