from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'lesson', views.LessonViewSet)
router.register(r'programm', views.ProgrammViewSet)
router.register(r'company ', views.CompanyViewSet)
router.register(r'test', views.TestViewSet)
router.register(r'evolution', views.EvaluationViewSet)
router.register(r'file', views.FileViewSet)
router.register(r'prize', views.PrizeViewSet)
router.register(r'fine', views.FineViewSet)
router.register(r'error', views.ErrorViewSet)
router.register(r'socialmedia', views.SocialMediaViewSet)
router.register(r'bestemployee', views.BestEmployeesViewSet)

urlpatterns = [
    path('', include(router.urls)),        
]