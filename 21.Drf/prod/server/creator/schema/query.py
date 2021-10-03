import graphene
from django.db.models import Q
from graphene_django.filter import DjangoFilterConnectionField

from creator.models import Author
from creator.schema.type import CreatorType, CreatorCountType, AuthorType


class CreatorQueryProject(graphene.ObjectType):
    all_authors = DjangoFilterConnectionField(CreatorCountType)
    author_by_name = graphene.List(CreatorType,name=graphene.String(required=True))
    all_author_in_project = graphene.List(AuthorType)

    def resolve_all_author_in_project(self,info):
        return Author.objects.exclude(is_superuser=True)

    def resolve_all_authors(self,info):
        return Author.objects.all()

    def resolve_author_by_name(self,info,name):
        filter_name = Q(username__icontains=name)
        qs= Author.objects.filter(filter_name)
        if not qs:
            return None
        return qs

