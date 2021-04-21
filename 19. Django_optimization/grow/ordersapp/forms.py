from django import forms
from django.forms import HiddenInput

from mainapp.models import GrowProducts
from ordersapp.models import Order, ItemInOrder


class BaseOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'user':
                field.widget = HiddenInput()
            field.widget.attrs['class'] = 'form-control'


class OrderForm(BaseOrderForm):
    class Meta:
        model = Order
        fields = ('user',)


class OrderItemForm(BaseOrderForm):
    price = forms.FloatField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = GrowProducts.get_items()
        self.fields['product'].queryset = products

    def clean_qty(self):
        item_count = self.cleaned_data.get('count')
        product = self.cleaned_data.get('product')
        if item_count > product.quantity:
            raise forms.ValidationError('недостаточно на складе!')
        return item_count

    class Meta:
        model = ItemInOrder
        fields = '__all__'
