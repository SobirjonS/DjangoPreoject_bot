from rest_framework import serializers
from . import models

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True)

    class Meta:
        model = models.News
        fields = ['id', 'author', 'title', 'body', 'created_at', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        news = models.News.objects.create(**validated_data)
        for image_data in images_data:
            models.NewsImage.objects.create(news=news, **image_data)
        return news

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        instance.images.all().delete()
        for image_data in images_data:
            models.NewsImage.objects.create(news=instance, **image_data)

        return instance