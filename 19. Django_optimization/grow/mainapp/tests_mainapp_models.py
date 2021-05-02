from django.test import TestCase
from mainapp.models import GrowProducts, GrowCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = GrowCategory.objects.create(name="test_category")
        self.product_1 = GrowProducts.objects.create(name="prod_1",
                                                     category=category,
                                                     price=1999.5,
                                                     count=150)

        self.product_2 = GrowProducts.objects.create(name="prod_2",
                                                     category=category,
                                                     price=2998.1,
                                                     count=125,
                                                     is_active=False)

        self.product_3 = GrowProducts.objects.create(name="prod_3",
                                                     category=category,
                                                     price=998.1,
                                                     count=115)

    def test_product_get(self):
        product_1 = GrowProducts.objects.get(name="prod_1")
        product_2 = GrowProducts.objects.get(name="prod_2")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = GrowProducts.objects.get(name="prod_1")
        product_2 = GrowProducts.objects.get(name="prod_2")
        self.assertEqual(str(product_1), 'prod_1')
        self.assertEqual(str(product_2), 'prod_2')

    def test_product_get_items(self):
        product_1 = GrowProducts.objects.get(name="prod_1")
        product_3 = GrowProducts.objects.get(name="prod_3")
        products = product_1.get_items()

        self.assertEqual(list(products), [product_1, product_3])
