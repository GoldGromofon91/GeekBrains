from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from creator.views import CreatorViewSet
from todo.views import ProjectViewSet, TodoViewSet

router = DefaultRouter()
router.register('creators', CreatorViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', TodoViewSet)

schema_view = get_schema_view(openapi.Info(
    title="Library",
    default_version='0.1',
    description="Documentation to out project", contact=openapi.Contact(email="admin@ex.ru"),
    license=openapi.License(name="MIT License"),
),
    public=True, permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token/', obtain_auth_token),
    path('api/token/jwt/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    re_path(r'^api/(?P<version>\d.\d)/', include(router.urls)),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
