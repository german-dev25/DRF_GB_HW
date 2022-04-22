from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    '''Представление на базе ModelViewSet, позволяющее использовать все
    REST API-запросы'''

    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

    pagination_class = ProjectLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return Project.objects.filter(name__contains=name)
        return Project.objects.all()
