from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from creator.models import Author
from creator.serializers import CreatorModelSerializer


class CreatorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = CreatorModelSerializer
