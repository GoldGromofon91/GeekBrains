from django.utils.functional import cached_property
from mainapp.models import GrowCategory


def categories(request):
    return {'category': GrowCategory.objects.filter(is_active=True)}

