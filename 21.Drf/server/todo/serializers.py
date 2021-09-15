from django.contrib.auth import get_user_model
from rest_framework import serializers

from creator.serializers import CreatorModelSerializer
from todo.models import Project, Todo


class ProjectModelSerializer(serializers.ModelSerializer):
    # users = serializers.PrimaryKeyRelatedField(many=True,queryset=get_user_model().objects.all())
    users = serializers.StringRelatedField(many=True)
    # users = serializers.CharField()
    class Meta:
        model = Project
        fields = "__all__"


class TodoModelSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    user = CreatorModelSerializer()

    class Meta:
        model = Todo
        fields = "__all__"

