import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import GrowCategory, GrowProducts


def get_category():
    return GrowCategory.objects.all()


def get_hot_prod():
    return random.choice(GrowProducts.objects.all())


def index(request):
    content = {'title_page': 'gy| главная'}
    return render(request, 'mainapp/index.html', context=content)


def contacts(request):
    content = {'title_page': 'gy| контакты'}
    return render(request, 'mainapp/contacts.html', context=content)


def house_grow(request):
    content = {'title_page': ' каталог',
               'category': get_category()
               }
    return render(request, 'mainapp/house.html', context=content)


def house_grow_products(request, pk):
    page_number = request.GET.get('page',1)
    category = get_object_or_404(GrowCategory, pk=pk)
    products = category.growproducts_set.all()

    products_paginator = Paginator(products, 2)
    try:
        products = products_paginator.page(page_number)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    content = {
        'page_title': 'товары категории',
        'categories': get_category(),
        'category': category,
        'products': products
    }
    return render(request, 'mainapp/category_products.html', context=content)


def product_page(request,pk):
    growproduct = get_object_or_404(GrowProducts,pk=pk)
    content = {
        'page_title': 'старнциа товара',
        'categories': get_category(),
        'product': growproduct
    }
    return render(request, 'mainapp/product_page.html', context=content)