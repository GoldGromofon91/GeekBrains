import random

from django.core.management.base import BaseCommand
from creator.models import Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('author_count', type=int)

    def handle(self, *args, **options):
        Author.objects.all().delete()
        cnt = options['author_count']
        for i in range(cnt):
            instance = Author.objects.create(username=f'User{i+1}',
                                             email=f'user{i+1}_mail@domain.com',
                                             birthday_year=random.randint(1700, 1800),
                                             last_name='Some last name',
                                             first_name='Some last name')

        print(f'done.Create {cnt} objects')
