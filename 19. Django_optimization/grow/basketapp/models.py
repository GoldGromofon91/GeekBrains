from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import GrowProducts


class GrowBasket(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='basket')
    product = models.ForeignKey(GrowProducts, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('количество', default=0)
    created_at = models.DateTimeField('время создания', auto_now_add=True)
    updated_at = models.DateTimeField('время обновления', auto_now=True)


    @property
    def prod_cost(self):
        return self.product.price * self.count