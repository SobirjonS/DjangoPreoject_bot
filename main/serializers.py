from rest_framework import serializers
from . import models

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, required=False)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.News
        fields = ['id', 'author', 'title', 'body', 'created_at', 'images']
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        news = models.News.objects.create(**validated_data)
        for image_data in images_data:
            models.NewsImage.objects.create(news=news, image=image_data)
        return news

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        if images_data:
            for old_image in instance.images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.NewsImage.objects.create(news=instance, image=image_data)

        return instance
    

class LessonImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonsImage
        fields = ['id', 'image']


class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LessonsVideo
        fields = ['id', 'video']

class LessonSerializer(serializers.ModelSerializer):
    images = LessonImageSerializer(many=True, required=False, read_only=True)
    videos = LessonVideoSerializer(many=True, required=False, read_only=True)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.Lesson
        fields = ['id', 'author', 'title', 'description', 'created_at', 'images', 'videos']
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        videos_data = self.context['request'].FILES.getlist('videos')
        lesson = models.Lesson.objects.create(**validated_data)
        for image_data in images_data:
            models.LessonsImage.objects.create(lesson=lesson, image=image_data)
        for video_data in videos_data:
            models.LessonsVideo.objects.create(lesson=lesson, video=video_data)
        return lesson

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        videos_data = self.context['request'].FILES.getlist('videos')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if images_data:
            for old_image in instance.images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.NewsImage.objects.create(news=instance, image=image_data)

        if videos_data:
            for old_video in instance.videos.all():
                old_video.video.delete()
                old_video.delete()

            for video_data in videos_data:
                models.Lesson.objects.create(lesson=instance, video=video_data)

        return instance
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProgrammImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProgrammsImage
        fields = ['id', 'image']

class ProgrammSerializer(serializers.ModelSerializer):
    images = ProgrammImageSerializer(many=True, required=False)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.Programm
        fields = ['id', 'author', 'title', 'body', 'created_at', 'images']
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        programm = models.Programm.objects.create(**validated_data)
        for image_data in images_data:
            models.ProgrammsImage.objects.create(programm=programm, image=image_data)
        return programm

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        if images_data:
            for old_image in instance.images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.ProgrammsImage.objects.create(programm=instance, image=image_data)

        return instance