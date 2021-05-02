from django.core.management.base import BaseCommand
from mainapp.models import GrowProducts
from django.db.models import Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        query_get_product = GrowProducts.objects.filter(
            Q(category__name='системы роста') |
            Q(category__name='удобрения')
        )
        for num,el in enumerate(query_get_product,1):
            print(f'{num}.{el.name} - {el.price}')
        print(f'Total query in db: {len(query_get_product)}')
