from rest_framework import status
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filters import TodoDateFilter
from .models import Todo
from .serializers import TodoModelSerializer


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(CreateModelMixin,
                       ListModelMixin,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       GenericViewSet):
    '''Представление на базе GenericViewSet, позволяющее использовать все
    выбранные REST API-запросы (аналогично ModelViewSet) с измененным
    миксином '''

    permission_classes = [DjangoModelPermissions]
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()

    pagination_class = TodoLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    filterset_class = TodoDateFilter

    def destroy(self, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = 0
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        project_name = self.request.query_params.get('name', None)
        if project_name:
            return Todo.objects.filter(project__name=project_name)
        return Todo.objects.all()

# при удалении To Do - флажок поля "В работе" переключается с "True" на "False"

