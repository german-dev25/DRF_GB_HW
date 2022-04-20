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


'''Сериализация модели Todo с
представление данных (проект и пользователь) 
в виде словарей, а не id'''
# class TodoModelSerializerToString(TodoModelSerializer):
#     # project = StringRelatedField()
#     # user = StringRelatedField()
