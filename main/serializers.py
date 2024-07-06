from rest_framework import serializers
from .models import News, NewsImage

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, required=False)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = News
        fields = ['id', 'author', 'title', 'body', 'created_at', 'images']
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        news = News.objects.create(**validated_data)
        for image_data in images_data:
            NewsImage.objects.create(news=news, image=image_data)
        return news

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        # Удалить старые изображения только если в запросе есть новые изображения
        if images_data:
            for old_image in instance.images.all():
                old_image.image.delete()  # Удалить файл с диска
                old_image.delete()

            for image_data in images_data:
                NewsImage.objects.create(news=instance, image=image_data)

        return instance
