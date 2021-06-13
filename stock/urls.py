from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_stock, name='stock'),
    path('<int:item_id>', views.item_details, name='item_details'),
    path('add/', views.add_item, name='add_item')
]

