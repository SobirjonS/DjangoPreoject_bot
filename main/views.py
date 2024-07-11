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
        for image in instance.news_images.all():
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
        for image in instance.lesson_images.all():
            image.image.delete()
            image.delete()

        for video in instance.lesson_videos.all():
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
        for image in instance.programm_images.all():
            image.image.delete()
            image.delete()
        instance.delete()


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        for image in instance.company_images.all():
            image.image.delete()
            image.delete()
        instance.delete()


class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PrizeViewSet(viewsets.ModelViewSet):
    queryset = models.Prize.objects.all()
    serializer_class = serializers.PrizeSerializer
    permission_classes = [IsAuthenticated]


class FineViewSet(viewsets.ModelViewSet):
    queryset = models.Fine.objects.all()
    serializer_class = serializers.FineSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = models.Error.objects.all()
    serializer_class = serializers.ErrorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user)


class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = models.SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer
    permission_classes = [IsAuthenticated]


class BestEmployeesViewSet(viewsets.ModelViewSet):
    queryset = models.BestEmployees.objects.all()
    serializer_class = serializers.BestEmployeesSerializer
    permission_classes = [IsAuthenticated]
