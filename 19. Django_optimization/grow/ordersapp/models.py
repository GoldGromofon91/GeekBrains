from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property

from mainapp.models import GrowProducts


class Order(models.Model):
    STATUS_FORMING = 'f'
    STATUS_SENDED = 's'
    STATUS_PAID = 'p'
    STATUS_CANCELED = 'c'

    STATUS_CHOICES = (
        (STATUS_FORMING, 'формируется'),
        (STATUS_SENDED, 'отправлен'),
        (STATUS_PAID, 'оплачен'),
        (STATUS_CANCELED, 'отменен'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField('время создания', db_index=True,auto_now_add=True)
    updated_at = models.DateTimeField('время обновления', auto_now=True)
    status = models.CharField('cтатус', max_length=1, db_index=True, choices=STATUS_CHOICES, default=STATUS_FORMING)
    is_active = models.BooleanField('активность заказа', db_index=True, default=True)

    @cached_property
    def get_item_in_order(self):
        return self.item_in_order.all()


    @cached_property
    def is_forming(self):
        return self.status == self.STATUS_FORMING

    @cached_property
    def summary_product(self):
        item = self.item_in_order.all()
        print(sum(map(lambda x: x.prod_cost, item)))
        return {
            'total_count': sum(map(lambda x: x.count, item)),
            'total_cost': sum(map(lambda x: x.prod_cost, item))
        }



    def delete(self, using=None, keep_parents=False):
        # Recovery, если не хотим удалять из БД
        # self.is_active = False
        # self.save()
        super().delete()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class ItemInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item_in_order')
    product = models.ForeignKey(GrowProducts, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('количество', default=0)
    created_at = models.DateTimeField('время создания', auto_now_add=True)
    updated_at = models.DateTimeField('время обновления', auto_now=True)

    @cached_property
    def prod_cost(self):
        return self.product.price * self.count

    @classmethod
    def get_item(cls,pk):
        return cls.objects.filter(pk=pk).first()
