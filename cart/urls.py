from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name='shopping_cart'),
    path('<item_id>', views.add_shopping, name='add_shopping'),
    path('<item_id>', views.update_shopping, name='add_shopping'),
]
