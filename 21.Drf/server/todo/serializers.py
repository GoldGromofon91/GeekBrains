from rest_framework import serializers

from creator.serializers import CreatorModelSerializer
from todo.models import Project, Todo


class ProjectModelSerializer(serializers.ModelSerializer):
    # users = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(serializers.ModelSerializer):
    project = serializers.CharField()
    text = serializers.CharField()

    class Meta:
        model = Todo
        fields = "__all__"

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)