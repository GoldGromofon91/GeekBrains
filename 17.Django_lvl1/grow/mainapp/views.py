from django.shortcuts import render


# Create your views here.
def index(request):
    title= {'title_page':'gy| главная'}
    return render(request, 'mainapp/index.html', context=title)


def contacts(request):
    title = {'title_page': 'gy| контакты'}
    return render(request, 'mainapp/contacts.html',context=title)


def house_grow(request):
    title = {'title_page': 'gy| теплица'}
    return render(request, 'mainapp/house.html',context=title)


def house_grow_products(request):
    """
    Метод отображения продуктов
    В дальнейшем после подключения models этот метод уже будет id продукта а по нему
    будем брать title,name
    """
    titles = {'title_page':'gy| your avocado'}

    gen_content = {
        'telegram': '@Grow',
        'instagramm': '@grow',
    }
    return render(request, 'mainapp/avo.html', context=titles)
