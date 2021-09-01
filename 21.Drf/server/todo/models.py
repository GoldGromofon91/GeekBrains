from django.contrib.auth import get_user_model
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=32, null=False)
    ref = models.CharField(max_length=128, null=True, blank=True)
    user = models.ManyToManyField(get_user_model())

    class Meta:
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_todo')
    text = models.TextField(max_length=1024)
    user = models.ForeignKey(get_user_model(), models.CASCADE, related_name='user_todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'todo'
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
