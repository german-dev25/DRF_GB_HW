from django.core.management.base import BaseCommand
from users.models import User


JSON_PATH = 'mainapp/json'


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Создаем суперпользователя при помощи менеджера модели
        User.objects.create_superuser(
            username='django',
            email='django@localhost',
            password='12345'
        )

        User.objects.create_user(
            username='test1',
            email='test1@localhost',
            password='12345'
        )

        User.objects.create_user(
            username='test2',
            email='test2@localhost',
            password='12345'
        )