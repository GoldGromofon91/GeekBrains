from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from todo.filter import ProjectFilter, TodoFilter
from todo.models import Project, Todo
from todo.pagination import ProjectLimitOffsetPagination, TodoLimitOffsetPagination
from todo.serializers import ProjectGetModelSerializer, TodoModelSerializer, ProjectAddEditModelSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectGetModelSerializer
        return ProjectAddEditModelSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter
