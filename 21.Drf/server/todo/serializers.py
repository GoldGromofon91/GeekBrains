from rest_framework import serializers

from creator.serializers import CreatorModelSerializer
from todo.models import Project, Todo


class ProjectModelSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(serializers.ModelSerializer):
    user = CreatorModelSerializer()
    project = ProjectModelSerializer()

    class Meta:
        model = Todo
        fields = "__all__"
