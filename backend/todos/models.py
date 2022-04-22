from django.db import models

from projects.models import Project
from users.models import User


class Todo(models.Model):
    DRAFT = 'DR'
    SUB_TO_WORK = 'TO'
    CHECK = 'CH'
    DONE = 'DO'
    CLOSE = 'X'

    STATUS_CHOICES = (
        (DRAFT, 'Черновик'),
        (SUB_TO_WORK, 'Передано в работу'),
        (CHECK, 'Проверяется'),
        (DONE, 'Выполнено'),
        (CLOSE, 'Закрыто'),
    )

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
    status = models.CharField(
        verbose_name='Статус',
        choices=STATUS_CHOICES,
        max_length=2,
        default='DR'
    )
    is_active = models.BooleanField(
        verbose_name='В работе',
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
