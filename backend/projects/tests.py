from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from projects.models import Project
from users.models import User
from projects.views import ProjectModelViewSet


class TestProjectViewSet(TestCase):

    def test_get_list(self):
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        factory = APIRequestFactory()

        request = factory.get('/api/projects/')
        force_authenticate(request, user)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_projects_user_count(self):
        user_1 = User.objects.create(username='Ivanov89',
                                     first_name='Иван',
                                     last_name='Иванов',
                                     email='ivanov@mail.ru')
        user_2 = User.objects.create(username='Petrov25',
                                     first_name='Петр',
                                     last_name='Петров',
                                     email='petrov@mail.ru')
        project = Project.objects.create(name='Проект 1')
        project.users.set([user_1.pk, user_2.pk])

        client = APIClient()
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        self.assertEqual(project.users.count(), 2)

