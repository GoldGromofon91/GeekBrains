import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('author_count', type=int)

    def handle(self, *args, **options):
        get_user_model().objects.all().delete()
        cnt = options['author_count']
        for i in range(cnt):
            user = get_user_model()(username=f'User{i + 1}',
                                    email=f'user{i + 1}_mail@domain.com',
                                    birthday_year=random.randint(1700, 1800),
                                    last_name='Some last name',
                                    first_name='Some last name'
                                    )
            user.set_password('geekbrains')
            user.save()
        print(f'done.Create {cnt} objects')
