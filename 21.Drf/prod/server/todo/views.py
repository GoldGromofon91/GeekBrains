from rest_framework.viewsets import ModelViewSet

from todo.filter import ProjectFilter, TodoFilter
from todo.models import Project, Todo
from todo.pagination import ProjectLimitOffsetPagination, TodoLimitOffsetPagination
from todo.serializers import ProjectGetModelSerializer, ProjectAddEditModelSerializer, \
    TodoGetModelSerializer, TodoAddEditModelSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectGetModelSerializer
        return ProjectAddEditModelSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.filter(is_active=True)
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TodoGetModelSerializer
        return TodoAddEditModelSerializer
