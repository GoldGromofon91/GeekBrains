
from rest_framework import serializers

from creator.models import Author


class CreatorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'username', 'email','first_name','last_name','birthday_year']
