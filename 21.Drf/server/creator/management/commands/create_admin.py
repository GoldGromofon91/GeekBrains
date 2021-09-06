import random

from django.conf import settings
from django.contrib.auth import get_user_model

from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        get_user_model().objects.create_superuser('django','django@mail.ru','geekbrains')
        return 'ADMIN create'