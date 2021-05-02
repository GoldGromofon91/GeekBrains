from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from mainapp.models import GrowCategory,GrowProducts


class TestMainappSmoke(TestCase):
    fixtures = ['main_db.json']

    @classmethod
    def setUpClass(cls):  # once
        super().setUpClass()
        cls.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('mainapp:category'))
        self.assertEqual(response.status_code, 200)

    def test_product_category_urls(self):
        response = self.client.get(reverse('mainapp:category'),kwargs={'pk':1})

        self.assertEqual(response.status_code, 200)
        for prod in GrowProducts.objects.all():
            response = self.client.get(
                reverse('mainapp:product_page',
                        kwargs={'pk': prod.pk})
            )
            self.assertEqual(response.status_code, 200)

    def test_product_urls(self):
        for product in GrowProducts.objects.all():
            response = self.client.get(f'/product/{product.pk}/')
            self.assertEqual(response.status_code, 200)
