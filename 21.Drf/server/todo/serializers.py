from django.contrib.auth import get_user_model
from rest_framework import serializers

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


class TodoModelSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    user = CreatorModelSerializer()

    class Meta:
        model = Todo
        fields = "__all__"
