import server.settings
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from creator.serializers import CreatorModelSerializer


class CreatorViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.UpdateModelMixin,viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = get_user_model().objects.exclude(is_superuser=True)
    serializer_class = CreatorModelSerializer