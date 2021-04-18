from django.contrib.auth import get_user_model
from django.db import models

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
    created_at = models.DateTimeField('время создания', auto_now_add=True)
    updated_at = models.DateTimeField('время обновления', auto_now=True)
    status = models.CharField('cтатус', max_length=1, choices=STATUS_CHOICES, default=STATUS_FORMING)
    is_active = models.BooleanField('активность заказа', default=True)

    @property
    def is_forming(self):
        return self.status == self.STATUS_FORMING

    @property
    def total_count(self):
        return sum(map(lambda x: x.count, self.item_in_order.all()))

    @property
    def total_cost(self):
        return sum(map(lambda x: x.prod_cost, self.item_in_order.all()))

    # переопределяем метод, удаляющий объект
    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

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

    @property
    def prod_cost(self):
        return self.product.price * self.count

