from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    email = models.CharField(max_length=64, unique=True)
    birthday_year = models.PositiveSmallIntegerField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
