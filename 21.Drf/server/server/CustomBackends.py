from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.forms import forms

from server import settings


class CustomBackends(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = get_user_model().objects.get(username=username)
            except get_user_model().DoesNotExist:
                return None
            return user
        return None

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data