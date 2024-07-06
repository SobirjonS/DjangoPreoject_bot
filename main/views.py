from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        # Удалить все связанные изображения
        for image in instance.images.all():
            image.image.delete()  # Удалить файл с диска
            image.delete()
        instance.delete()
