from rest_framework.relations import StringRelatedField

from .models import Project
from rest_framework.serializers import ModelSerializer


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        exclude = (
            'created',
            'updated',
        )


'''Сериализация модели Проекта c 
представлением данных (пользователи) 
в виде словарей, а не id'''
# class ProjectModelSerializerToString(ProjectModelSerializer):
#     users = StringRelatedField(many=True)
