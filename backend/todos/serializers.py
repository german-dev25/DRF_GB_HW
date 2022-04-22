from rest_framework.relations import StringRelatedField

from .models import Todo
from rest_framework.serializers import ModelSerializer


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        exclude = (
            'created',
            'updated',
        )
    project = StringRelatedField()
    user = StringRelatedField()
