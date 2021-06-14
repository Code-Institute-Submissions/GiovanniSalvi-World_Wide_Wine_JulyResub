from django import forms
from .models import Item, Stock


class StockForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        stock_fields = Stock.objects.all()
        types = [(f.id, f.types) for f in stock_fields]

        

        