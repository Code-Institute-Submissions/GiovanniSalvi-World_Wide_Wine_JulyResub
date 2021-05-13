from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name='shopping_cart'),
    path('add/<item_id>', views.add_shopping, name='add_shopping'),
    path('update/<item_id>', views.update_cart, name='update_cart'),
]
