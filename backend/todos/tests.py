from django.test import TestCase
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from users.models import User
from .models import Todo

from todos.views import TodoModelViewSet


class TestTodoViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todos/')
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, user)
        view = TodoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTodoPutAndGet(APITestCase):

    def test_todo_mixer_and_put(self):
        todo = mixer.blend(Todo)
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')

        response = self.client.put(f'/api/todos/{todo.id}/', {'text': 'Текст заметки 1', 'is_active': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo = Todo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'Текст заметки 1')
        self.assertEqual(todo.is_active, True)