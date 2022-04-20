from django.db import models

from users.models import User


class Project(models.Model):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['is_done', '-created', 'name']

    name = models.CharField(
        verbose_name='Название',
        max_length=32,
        blank=False,
        null=False,
    )
    href_repository = models.URLField(
        verbose_name='URL репозитория',
        max_length=128,
        default='',
    )
    users = models.ManyToManyField(
        User,
        verbose_name='Участники проекта',
    )
    is_done = models.BooleanField(
        verbose_name='Готовность',
        default='True',
    )
    created = models.DateTimeField(
        verbose_name='Создан',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Изменен',
        auto_now=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'
