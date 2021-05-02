from django.test import TestCase, Client

from authapp.models import GrowUser


class TestUserManagement(TestCase):
    fixtures = ['authapp.json']

    def setUp(self):
        self.client = Client()
        self.superuser = GrowUser.objects.create_superuser(
            'django2', 'django2@geekshop.local', 'geekbrains'
        )
        self.user = GrowUser.objects.create_user(
            'usettest1', 'ut1@example.com', 'geekbrains'
        )
        self.user_with__first_name = GrowUser.objects.create_user(
            'usertest2', 'ut2@example.com', 'geekbrains', first_name='User'
        )

    def test_user_login(self):
        # главная без логина
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertEqual(response.context['title_page'], 'gy| главная')
        self.assertNotContains(response, 'Пользователь', status_code=200)

        # Логин пользователя с данными
        self.client.post('/auth/login/',
                         data={'username': 'usettest1',
                               'password': 'geekbrains'})
        self.client.login(username='tarantino', password='geekbrains')

        # главная после логина
        response = self.client.get('/')
        self.assertEqual(self.user, response.context['user'])
        self.assertContains(response, 'Пользователь', status_code=200)

    def test_basket_login_redirect(self):

        response = self.client.get('/basket/')
        self.assertEqual('/auth/login/?next=/basket/', response.url)
        self.assertEqual(302, response.status_code)

        self.client.login(username='usertest2', password='geekbrains')

        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([], list(response.context['user'].get_element))
        self.assertEqual('/basket/', response.request['PATH_INFO'])

    def test_user_logout(self):
        self.client.login(username='usertest2', password='geekbrains')

        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)

        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)

    def test_user_register(self):
        response = self.client.get('/auth/user/register/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('регистрация', response.context['title_page'])
        self.assertTrue(response.context['user'].is_anonymous)

        new_user_obj = {
            'username': 'usertest3New',
            'first_name': 'Usertest3',
            'last_name': 'Usertest3',
            'password1': 'geekbrains',
            'password2': 'geekbrains',
            'email': 'ut3@example.com',
            'age': '20'
        }

        response = self.client.post('/auth/user/register/', data=new_user_obj)
        self.assertEqual(response.status_code, 200)
        new = GrowUser(username=new_user_obj['username'],password=new_user_obj['password1'])
        new.save()

        new_user = GrowUser.objects.get(username=new_user_obj['username'])
        self.assertTrue(new_user.is_active)

    #     activation_url = f"{settings.DOMAIN_NAME}/auth/user/verify/{new_user_obj['email']}/" \
    #                      f"{new_user.activation_key}/"
    #
    #     response = self.client.get(activation_url)
    #     self.assertEqual(response.status_code, 200)
    # #
        # данные нового пользователя
    #     self.client.login(
    #         username=new_user_obj['username'],
    #         password=new_user_obj['password1']
    #     )
    # #
    #     # проверяем главную страницу
    #     response = self.client.get('/')
    #     self.assertContains(response, text=new_user_obj['first_name'], status_code=200)

    # def test_user_wrong_register(self):
    #     new_user_data = {
    #         'username': 'teen',
    #         'first_name': 'Мэри',
    #         # 'last_name': 'Поппинс',
    #         'password1': 'geekbrains',
    #         'password2': 'geekbrains',
    #         'email': 'merypoppins@geekshop.local',
    #         'age': '17'
    #     }
    #
    #     response = self.client.post('/auth/user/register/', data=new_user_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(
    #         response, 'form', 'age', 'Вы слишком молоды!'
    #     )
    #     # with self.assertRaises(ValidationError) as e:
    #     #     pass
