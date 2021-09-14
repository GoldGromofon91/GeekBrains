from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from creator.views import CreatorViewSet
from todo.views import ProjectViewSet, TodoViewSet

router = DefaultRouter()
router.register('creators',CreatorViewSet)
router.register('projects',ProjectViewSet)
router.register('todo',TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token/', obtain_auth_token),
    path('api/',include(router.urls)),
    path('api/token/jwt/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

