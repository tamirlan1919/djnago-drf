from django.urls import path
from planner.views import HiApiView, TaskListApiView, TaskDetailApiView, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('hello/', HiApiView.as_view()),
    *router.urls
    
]