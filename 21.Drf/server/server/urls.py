from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from creator.views import CreatorViewSet
from todo.views import ProjectViewSet, TodoViewSet

router = DefaultRouter()
router.register('creators',CreatorViewSet)
router.register('projects',ProjectViewSet)
router.register('todo',TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
