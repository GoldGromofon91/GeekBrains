from django.core.management.base import BaseCommand
from mainapp.models import GrowProducts,GrowCategory
from authapp.models import GrowUser

import json, os

JSON_PATH = 'mainapp/json/'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        GrowCategory.objects.all().delete()
        for category in categories:
            new_category = GrowCategory(**category)
            new_category.save()

        products = load_from_json('products')

        GrowProducts.objects.all().delete()
        for product in products:
            category_name = product["category"]

            _category = GrowCategory.objects.get(name=category_name)

            product['category'] = _category
            new_product = GrowProducts(**product)
            new_product.save()

        if not GrowUser.objects.filter(username='django'):
            GrowUser.objects.create_superuser('django','example@mail.ru','geekbrains')
