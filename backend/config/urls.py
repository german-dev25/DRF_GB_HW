from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views import UserModelViewSet
from projects.views import ProjectModelViewSet
from todos.views import TodoModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Todo",
        default_version='0.2',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-auth-token/', views.obtain_auth_token),
    path('jwt-token-refresh/', TokenRefreshView.as_view()),
    path('jwt-token/', TokenObtainPairView.as_view()),

    # UrlPathVersioning
    # re_path(r'^api/(?P<version>\d\.\d)/users/$', UserModelViewSet.as_view({'get': 'list'}))

    # NamespaceVersioning
    path('api/', include('users.urls')),
    path('api/0.1/', include('users.urls', namespace='0.1')),
    path('api/0.2/', include('users.urls', namespace='0.2')),

    path('swagger/', schema_view.with_ui()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),

    path('redoc/', schema_view.with_ui('redoc')),
]
