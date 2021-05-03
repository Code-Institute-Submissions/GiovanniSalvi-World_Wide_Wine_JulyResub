from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stock, name='stock'),
    path('<item_id>', views.item_details, name='item_details')
]
