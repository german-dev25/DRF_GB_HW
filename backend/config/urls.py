from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views import UserModelViewSet
from projects.views import ProjectModelViewSet
from todos.views import TodoModelViewSet

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
]
