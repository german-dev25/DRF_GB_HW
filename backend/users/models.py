from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    username = models.CharField(
        verbose_name='Никнейм',
        max_length=64,
        blank=True,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=64,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=64,
        blank=True,
    )
    birthday = models.DateField(
        verbose_name='День Рождения',
        max_length=10,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Эл.почта',
        max_length=64,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return f'{self.username}'
