from rest_framework import serializers, status
from rest_framework.response import Response

from creator.serializers import CreatorModelSerializer
from todo.models import Project, Todo


class ProjectGetModelSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ProjectAddEditModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TodoGetModelSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    user = CreatorModelSerializer()

    class Meta:
        model = Todo
        fields = "__all__"

class TodoAddEditModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"