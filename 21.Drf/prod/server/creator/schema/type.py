import graphene
from graphene import Node, Connection
from graphene_django import DjangoObjectType

from creator.models import Author
from todo.schema.type import ProjectType


class CreatorType(DjangoObjectType):
    class Meta:
        model = Author
        exclude = ('is_superuser', 'password')


class CreatorCountConnection(Connection):
    class Meta:
        abstract = True

    all_count_author = graphene.Int()

    def resolve_all_count_author(self, info):
        return self.iterable.count()


class CreatorCountType(DjangoObjectType):
    class Meta:
        model = Author
        exclude = ('is_superuser', 'password')
        filter_fields = {
            'id': ['exact', ],
        }
        interfaces = (Node,)
        connection_class = CreatorCountConnection


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        exclude = ('is_superuser', 'is_staff', 'password')

    project = graphene.List(ProjectType)

    def resolve_project(self, info):
        return self.user_to_project.all()
