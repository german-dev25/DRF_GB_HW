from django.db import models

from projects.models import Project
from users.models import User


class Todo(models.Model):
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['is_active', '-created', 'project']
        unique_together = (('user', 'text', 'project'),)

    project = models.ForeignKey(
        Project,
        verbose_name='',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        verbose_name='',
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name='Текст заметки',
        max_length=512,
        blank=False,
    )
    is_active = models.BooleanField(
        verbose_name='Статус',
        default=False,
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Пользователь {self.user} создал {self.project} заметку - {self.text}'
