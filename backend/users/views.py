from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import GenericViewSet
from config.settings import REST_FRAMEWORK

from .models import User
from .serializers import UserModelSerializer


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = REST_FRAMEWORK['PAGE_SIZE']


class UserModelViewSet(ListModelMixin,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       GenericViewSet,
                       ):
    '''Возможность просмотра списка и каждого пользователя в
    отдельности, можно вносить изменения, нельзя удалять и создавать
    на базе GenericViewSet'''

    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    pagination_class = UserLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

