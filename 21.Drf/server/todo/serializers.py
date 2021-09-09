from rest_framework import serializers

from creator.serializers import CreatorModelSerializer
from todo.models import Project, Todo


class ProjectModelSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    project = serializers.CharField()

    class Meta:
        model = Todo
        fields = "__all__"
