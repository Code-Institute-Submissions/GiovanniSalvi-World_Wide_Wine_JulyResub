from django.shortcuts import render

# Create your views here.


def myaccount(request):

    template = 'myaccount/myaccount.html'
    context = {}

    return render(request, template, context)
