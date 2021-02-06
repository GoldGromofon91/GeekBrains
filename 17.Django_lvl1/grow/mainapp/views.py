from django.shortcuts import render

from mainapp.models import GrowCategory,GrowProducts


# Create your views here.
def index(request):
    content = {'title_page': 'gy| главная'}
    return render(request, 'mainapp/index.html', context=content)


def contacts(request):
    content = {'title_page': 'gy| контакты'}
    return render(request, 'mainapp/contacts.html', context=content)


def house_grow(request):
    title = 'каталог'
    category = GrowCategory.objects.all()
    content = {'title_page': title,
               'category': category}
    return render(request, 'mainapp/house.html', context=content)


def house_grow_products(request,pk):
    return render(request, 'mainapp/avo.html')


