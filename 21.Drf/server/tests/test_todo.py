import json

from django.contrib.auth import get_user_model
from mixer.auto import mixer
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import Project, Todo


class TestTodoViewSet(APITestCase):
    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser('django', 'admin@ex.ru', 'geekbrains')
        self.user = get_user_model().objects.create_user('user_test', 'user_test@example.ru', 'geekbrains')

    def test_list_project_authorized(self):
        self.client.force_login(user=self.superuser)
        response = self.client.get('/api/projects/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_todo_authorized(self):
        self.client.force_login(user=self.superuser)
        response = self.client.get('/api/todo/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_authorized(self):
        todo = mixer.blend(Todo, user__username='Savva')
        self.client.force_login(user=self.superuser)
        response = self.client.get(f'/api/todo/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_book = json.loads(response.content)
        self.assertEqual(response_book['user']['username'], 'Savva')

    # def test_project_authorized(self):
    #     project = mixer.blend(Project)
    #     self.client.force_login(user=self.superuser)
    #     response = self.client.put(f'/api/project/{project.id}/',
    #                               {'name': 'Test Project', 'ref': 'some ref','users':project.user_to_project.author.id})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     project = Project.objects.get(id=project.id)
    #     self.assertEqual(project.name, 'Test Project')