import django_filters
from django.db.models import Q

from todo.models import Project, Todo


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilter(django_filters.FilterSet):
    project__name = django_filters.CharFilter(lookup_expr='iexact')
    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='created_at__gt')
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='created_at__lt')

    class Meta:
        model = Todo
        fields = ['project']