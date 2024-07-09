from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        for image in instance.images.all():
            image.image.delete()
            image.delete()
        instance.delete()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        for image in instance.images.all():
            image.image.delete()
            image.delete()
        instance.delete()

        for video in instance.videos.all():
            video.video.delete()
            video.delete()
        instance.delete()


class ProgrammViewSet(viewsets.ModelViewSet):
    queryset = models.Programm.objects.all()
    serializer_class = serializers.ProgrammSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        for image in instance.images.all():
            image.image.delete()
            image.delete()
        instance.delete()
