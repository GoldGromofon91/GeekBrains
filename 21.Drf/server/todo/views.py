from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todo.models import Project, Todo
from todo.serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
