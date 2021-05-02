from django.core.management import BaseCommand
from django.db.models import Q

from datetime import timedelta
from django.db.models import F, When, Case, IntegerField, DecimalField
from ordersapp.models import ItemInOrder


class Command(BaseCommand):
    def handle(self, *args, **options):
        ID_SALE_1 = 1
        ID_SALE_2 = 2
        ID_SALE_3 = 3

        ttl_sale1__dt = timedelta(hours=12)
        ttl_sale2__dt = timedelta(hours=24)

        disc_sale1 = 0.25
        disc_sale2 = 0.10
        disc_sale3 = 0.05

        sale1__cond = Q(
            order__updated_at__lte=F('order__created_at') + ttl_sale1__dt
        )
        sale2__cond = Q(
            order__updated_at__gt=F('order__created_at') + ttl_sale1__dt
        ) & Q(
            order__updated_at__lte=F('order__created_at') + ttl_sale2__dt
        )
        sale3__cond = Q(
            order__updated_at__gt=F('order__created_at') + ttl_sale2__dt
        )

        sale1__order = When(sale1__cond, then=ID_SALE_1)
        sale2__order = When(sale2__cond, then=ID_SALE_2)
        sale3__order = When(sale3__cond, then=ID_SALE_3)

        sale1_change__price = When(sale1__cond,
                               then=F('product__price') * F('count') * disc_sale1)
        sale2_change__price = When(sale2__cond,
                               then=F('product__price') * F('count') * -disc_sale2)
        sale3_change__price = When(sale3__cond,
                                     then=F('product__price') * F('count') * disc_sale3)

        best_item_in_oreder = ItemInOrder.objects.annotate(
            action_order=Case(
                sale1__order,
                sale2__order,
                sale3__order,
                output_field=IntegerField(),
            )).annotate(
            discount=Case(
                sale1_change__price,
                sale2_change__price,
                sale3_change__price,
                output_field=DecimalField(),
            )).order_by('action_order', 'discount'). \
            select_related('order', 'product')

        for orderitem in best_item_in_oreder:
            print(f'{orderitem.action_order:2}: заказ №{orderitem.pk:3}:\
                   {orderitem.product.name:20}: скидка\
                   {abs(orderitem.discount):6.2f} руб. | \
                   {orderitem.order.updated_at - orderitem.order.created_at}')
