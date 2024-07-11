from rest_framework import serializers
from . import models

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    news_images = NewsImageSerializer(many=True, required=False, read_only=True)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.News
        fields = ['id', 'author', 'title', 'body', 'created_at', 'news_images']
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
            for old_image in instance.news_images.all():
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
    lesson_images = LessonImageSerializer(many=True, required=False, read_only=True)
    lesson_videos = LessonVideoSerializer(many=True, required=False, read_only=True)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.Lesson
        fields = ['id', 'author', 'title', 'description', 'created_at', 'lesson_images', 'lesson_videos']
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
            for old_image in instance.lesson_images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.LessonsImage.objects.create(lesson=instance, image=image_data)

        if videos_data:
            for old_video in instance.lesson_videos.all():
                old_video.video.delete()
                old_video.delete()

            for video_data in videos_data:
                models.LessonsVideo.objects.create(lesson=instance, video=video_data)

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
    programm_images = ProgrammImageSerializer(many=True, required=False, read_only=True)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.Programm
        fields = ['id', 'author', 'title', 'body', 'created_at', 'programm_images']
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
            for old_image in instance.programm_images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.ProgrammsImage.objects.create(programm=instance, image=image_data)

        return instance
    

class CompanyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyImage
        fields = ['id', 'image']

class CompanySerializer(serializers.ModelSerializer):
    company_images = CompanyImageSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Company
        fields = ['id', 'name', 'email', 'phone_number', 'location', 'working_hours', 'goal', 'value', 'company_images']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        company = models.Company.objects.create(**validated_data)
        for image_data in images_data:
            models.CompanyImage.objects.create(company=company, image=image_data)
        return company

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.location = validated_data.get('location', instance.location)
        instance.working_hours = validated_data.get('working_hours', instance.working_hours)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.value = validated_data.get('value', instance.value)
        instance.save()

        if images_data:
            for old_image in instance.company_images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.CompanyImage.objects.create(company=instance, image=image_data)

        return instance
    

class TestSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.Test
        fields = '__all__'


class EvaluationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = models.Evaluation
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.File
        fields = '__all__'


class PrizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prize
        fields = '__all__'


class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fine
        fields = '__all__'


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Error
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialMedia
        fields = '__all__'


class BestEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BestEmployees
        fields = '__all__'