from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import GrowBasket
from grow.settings import LOGIN_URL


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
def add_prod(request, pk):
    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:product_page',kwargs={'pk': pk}))

    basket_item, _ = GrowBasket.objects.get_or_create(user=request.user, product_id=pk)
    basket_item.count += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_prod(request, basket_elem_pk):
    basket_elem = get_object_or_404(GrowBasket, pk=basket_elem_pk)
    basket_elem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def update_count_prod(request, el_item_pk, el_item_count):
    if request.is_ajax():
        item = GrowBasket.objects.filter(pk=el_item_pk).first()
        if not item:
            return JsonResponse({'status': False})
        if el_item_count == 0:
            item.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            item.count = el_item_count
            item.save()

        basket_summary_html = render_to_string(
            'basketapp/includes/basket_summary.html',
            request=request
        )

        basket_prod_html = render_to_string(
            'basketapp/includes/basket_record.html',
            request=request
        )
        return JsonResponse({'status': True,
                             'basket_summary': basket_summary_html,
                             'count': el_item_count,
                             'basket_cost': basket_prod_html})
