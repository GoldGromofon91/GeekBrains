from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from creator.views import CreatorViewSet

router = DefaultRouter()
router.register('creator',CreatorViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
