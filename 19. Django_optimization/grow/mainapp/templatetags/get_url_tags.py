from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='url_prod_img')
def media_folder_products(string):
    if not string:
        string = 'prod_img/prod_def.png'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='url_user_img')
def media_folder_users(string):

    if not string:
        string = 'users_avatar/avatar.png'

    return f'{settings.MEDIA_URL}{string}'

