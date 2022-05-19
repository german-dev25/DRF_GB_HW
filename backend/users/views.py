from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import GenericViewSet
from config.settings import REST_FRAMEWORK

from .models import User
from .serializers import UserModelSerializer, UserModelSerializerWithStatus


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

    permission_classes = [DjangoModelPermissions]
    serializer_class = UserModelSerializer

    queryset = User.objects.all()

    pagination_class = UserLimitOffsetPagination
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.request.version is None or self.request.version == '0.2':
            return UserModelSerializerWithStatus
        return UserModelSerializer

