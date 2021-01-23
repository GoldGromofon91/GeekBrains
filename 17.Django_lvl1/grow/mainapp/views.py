from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def house_grow(request):
    return render(request, 'mainapp/house.html')


def house_grow_products(request):
    """
    Метод отображения продуктов
    """
    return render(request, 'mainapp/avo.html')
