from django import forms
from .models import MyAccount


class AccountForm(forms.ModelForm):
    class Meta:
        model = MyAccount
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number':'Phone Number',
            'default_city':'City',
            'default_postcode':'Post Code',
            'default_address':'Address',
            'default_country':'Country',
        }

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'account-form'
            self.fields[field].label = False
            
