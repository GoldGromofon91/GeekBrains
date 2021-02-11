from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from basketapp.models import GrowBasket


@login_required
def index(request):
    basket_user = request.user.basket.all()
    print(basket_user.count())
    content = {'title_page': 'корзина',
               'basket_user': basket_user,
               'count': basket_user.count(),
               }
    return render(request, 'basketapp/index.html', context=content)


@login_required
def add_prod(request,pk):
    basket_item, _ = GrowBasket.objects.get_or_create(user=request.user,product_id=pk)
    basket_item.count += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_prod(request,basket_elem_pk):
    basket_elem = get_object_or_404(GrowBasket, pk=basket_elem_pk)
    basket_elem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
