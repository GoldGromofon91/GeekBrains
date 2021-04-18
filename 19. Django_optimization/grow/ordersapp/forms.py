from django import forms
from django.forms import HiddenInput

from ordersapp.models import Order, ItemInOrder


class BaseOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'user':
                field.widget = HiddenInput()
            field.widget.attrs['class'] = f'form-control {field_name}'


class OrderForm(BaseOrderForm):
    class Meta:
        model = Order
        fields = ('user',)


class OrderItemForm(BaseOrderForm):
    class Meta:
        model = ItemInOrder
        fields = '__all__'
