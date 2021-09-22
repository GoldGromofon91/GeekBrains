# from creator.models import Author
from django.contrib.auth import get_user_model
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=32, null=False)
    ref = models.CharField(max_length=128, null=True, blank=True)
    users = models.ManyToManyField(get_user_model(),related_name='user_to_project')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_todo')
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), models.CASCADE, related_name='user_todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def delete(self):
        self.is_active = False
        self.save()
