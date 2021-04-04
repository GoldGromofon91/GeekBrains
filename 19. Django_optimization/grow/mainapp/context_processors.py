from mainapp.models import GrowCategory


def categories(request):
    return {'category':GrowCategory.objects.all()}