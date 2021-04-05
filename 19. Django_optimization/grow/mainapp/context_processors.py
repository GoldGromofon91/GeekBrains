from django.contrib.auth import get_user_model

from grow.settings import DOMAIN_NAME
from mainapp.models import GrowCategory


def categories(request):
    return {'category': GrowCategory.objects.all()}


# def message_accept_link(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         user = get_user_model().objects.get(username=username)
#         return {'message': f'{DOMAIN_NAME}/auth/user/verify/{user.email}/{user.activation_key}'}
