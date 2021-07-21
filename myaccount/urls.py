from django.urls import path
from . import views

urlpatterns = [
    path('', views.myaccount, name='myaccount'),
    path('remove/<order_number>', views.remove_order, name='remove_order'),
]
