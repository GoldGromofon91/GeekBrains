from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from creator.serializers import CreatorModelSerializer, CreatorModelSerializer_v2_0


class CreatorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, viewsets.GenericViewSet):

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = get_user_model().objects.exclude(is_superuser=True)

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return CreatorModelSerializer_v2_0
        return CreatorModelSerializer
