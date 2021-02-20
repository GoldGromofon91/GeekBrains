from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import HiddenInput, forms
from authapp.forms import GrowUserChangeForm
from mainapp.models import GrowCategory, GrowProducts

from django.forms import ModelForm


class GrowAdminChangeForm(GrowUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'password', 'email', 'age_user', 'avatar_user', 'is_staff',
            'is_superuser',
            'is_active')


class GrowCategoryUpdateForm(GrowUserChangeForm):
    class Meta:
        model = GrowCategory
        fields = ('name', 'description', 'is_active')


class GrowCategoryAdminCreateForm(ModelForm):
    class Meta:
        model = GrowCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class GrowProductsAdminCreateForm(ModelForm):
    class Meta:
        model = GrowProducts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'category':
                field.widget = HiddenInput()

