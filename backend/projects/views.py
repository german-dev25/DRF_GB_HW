from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectModelSerializer


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

