from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    UpdateUserAPIView,
    
)

urlpatterns = [
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('update/',UpdateUserAPIView.as_view(),name='update-user')
]