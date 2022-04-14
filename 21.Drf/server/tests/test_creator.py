from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from creator.models import Author
from creator.views import CreatorViewSet


class TestCreatorViewSet(TestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser('django', 'admin@ex.ru', 'geekbrains')
        self.user = get_user_model().objects.create_user('user_test', 'user_test@example.ru', 'geekbrains')
        self.creator_data = {
            'username':'Guest',
            'last_name': 'Guest_Last_Name',
            'first_name': 'Guest_First_Name',
            'birthday_year': 2000
        }
        self.creator_data_upd = {
            'username': "Savva",
            'last_name': 'ChangeLstName',
            'first_name': 'ChangeFstName',
            'birthday_year': 2005
        }

    def test_get_list_creator(self):
        factory = APIRequestFactory()
        request = factory.get('api/creators/')
        view = CreatorViewSet.as_view({'get': 'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_list_authorizated(self):
        factory = APIRequestFactory()
        request = factory.get('/api/creators/')
        force_authenticate(request, user=self.user)
        view = CreatorViewSet.as_view({'get': 'list'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_unauthorizated(self):
        author = Author.objects.create(username='Savva', birthday_year=1991)
        client = APIClient()

        response = client.get(f'/api/creators/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detail_authorizated(self):
        author = Author.objects.create(username='Savva', birthday_year=1991)
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get(f'/api/creators/{author.id}/')
        # print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_detail_unauthorizated(self):
        author = Author.objects.create(**self.creator_data)
        client = APIClient()
        client.login(username='User1', password='geekbrains')
        response = client.put(f'/api/creators/{author.id}/',
                              self.creator_data_upd)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_detail_authorizated(self):
        author = Author.objects.create(**self.creator_data)
        client = APIClient()
        client.login(username='django', password='geekbrains')
        response = client.patch(f'/api/creators/{author.id}/',data=self.creator_data_upd)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.first_name, self.creator_data_upd['first_name'])
        self.assertEqual(author.last_name, self.creator_data_upd['last_name'])
        self.assertEqual(author.birthday_year, self.creator_data_upd['birthday_year'])
        client.logout()
