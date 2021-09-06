from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from creator.models import Author
from creator.serializers import CreatorModelSerializer


class CreatorViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = CreatorModelSerializer

    def list(self, request):
        creator = Author.objects.all()
        serializer = CreatorModelSerializer(creator, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        creator = get_object_or_404(Author, pk=pk)
        serializer = CreatorModelSerializer(creator)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        creator = get_object_or_404(Author, pk=pk)
        serializer = CreatorModelSerializer(creator,data=request.data,partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
