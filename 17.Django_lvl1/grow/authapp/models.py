from django.contrib.auth.models import AbstractUser
from django.db import models


class GrowUser(AbstractUser):
    age_user = models.PositiveIntegerField('возраст', null=True)
    avatar_user = models.ImageField(upload_to='users_avatar', blank=True)

    def basket_element_price(self):
        return sum(el.prod_cost for el in self.basket.all())

    def basket_element_count(self):
        return sum(el.count for el in self.basket.all())
