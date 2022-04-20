from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoModelSerializer


class TodoModelViewSet(ModelViewSet):
    serializer_class = TodoModelSerializer
    queryset = Todo.objects.all()