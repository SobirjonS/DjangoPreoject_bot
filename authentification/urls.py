from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    UpdateUserAPIView,
    DeleteAPIView,
)

urlpatterns = [
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('update/',UpdateUserAPIView.as_view(),name='update-user'),
    path('delete/',DeleteAPIView.as_view(),name='delete-user')
]