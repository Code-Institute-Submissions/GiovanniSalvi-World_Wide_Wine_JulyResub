from django.shortcuts import render

# Create your views here.


def view_contact(request):

    """ A view that renders the contact form page """

    return render(request, 'contact/contactForm.html')
