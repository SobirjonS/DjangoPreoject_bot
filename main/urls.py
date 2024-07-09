from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'lesson', views.LessonViewSet)
router.register(r'programm', views.ProgrammViewSet)

urlpatterns = [
    path('', include(router.urls)),        
]