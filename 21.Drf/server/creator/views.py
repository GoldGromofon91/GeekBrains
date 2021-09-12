import server.settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from creator.serializers import CreatorModelSerializer


class CreatorViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = get_user_model().objects.all()
    serializer_class = CreatorModelSerializer

    def list(self, request):
        creator = get_user_model().objects.exclude(username=server.settings.ADMIN_LOGIN)
        serializer = CreatorModelSerializer(creator, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        creator = get_object_or_404(get_user_model(), pk=pk)
        serializer = CreatorModelSerializer(creator)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        creator = get_object_or_404(get_user_model(), pk=pk)
        serializer = CreatorModelSerializer(creator,data=request.data,partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
