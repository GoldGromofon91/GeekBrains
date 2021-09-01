from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    username = models.CharField(max_length=128, unique=True, null=False, blank=False)
    email = models.CharField(max_length=64, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    birthday_year = models.PositiveSmallIntegerField(null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'author'
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
