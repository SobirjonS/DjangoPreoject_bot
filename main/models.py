from django.db import models
from django.utils import timezone

from authentification.models import CustomUser


class Category(models.Model):
    section = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk}) {self.section} - {self.name}"
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории" 


class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='main/news_images/', null=True, blank=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.pk}) {self.author.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"  


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/news_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.pk}) {self.news.title}"
    
    class Meta:
        verbose_name = "Новостная изображение"
        verbose_name_plural = "Новостная изображения"  


class Lesson(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='main/lesson_images/', null=True, blank=True)
    video = models.FileField(upload_to='main/lesson_videos/', null=True, blank=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.pk}) {self.author.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"  


class LessonsImage(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/lesson_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.pk}) {self.lesson.title}"
    
    class Meta:
        verbose_name = "Изображение урока"
        verbose_name_plural = "Изображения урока" 


class LessonsVideo(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    video = models.FileField(upload_to='main/lesson_videos/', null=True, blank=True)

    def __str__(self):
        return f"{self.pk}) {self.lesson.title}"
    
    class Meta:
        verbose_name = "Видео урока"
        verbose_name_plural = "Видео урока" 


class Test(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.pk}) {self.author.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"  


class Evaluation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True, blank=True)
    test_title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(default=timezone.now)
    point = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.test:
            self.test_title = self.test.title
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pk}) {self.user.username} - {self.test_title}"
    
    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class File(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='main/files/')
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.pk}) {self.author.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"  


class Programm(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='main/news_images/', null=True, blank=True)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.pk}) {self.author.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"       


class ProgrammsImage(models.Model):
    programm = models.ForeignKey(Programm, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='main/programm_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.pk}) {self.programm.title}"
    
    class Meta:
        verbose_name = "Изображение программы"
        verbose_name_plural = "Изображеня программы"   


class Prize(models.Model):
    created_at = models.DateField()
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantum = models.FloatField()
    appointed_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk}) {self.employee.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Премию"
        verbose_name_plural = "Премии"  


class Fine(models.Model):
    created_at = models.DateField()
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantum = models.FloatField()
    appointed_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk}) {self.employee.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Штраф"
        verbose_name_plural = "Штрафы"  


class Error(models.Model):
    created_at = models.DateField()
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    why_happen = models.TextField()
    how_solved = models.TextField()
    prevent = models.TextField()

    def __str__(self):
        return f"{self.pk}) {self.employee.first_name} - {self.title}"
    
    class Meta:
        verbose_name = "Ошибка"
        verbose_name_plural = "Ошибки"  


class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)
    goal = models.TextField()
    value = models.TextField()

    def __str__(self):
        return f"{self.pk}) {self.name}"
    
    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании" 


class CompanyImage(models.Model):
    image = models.ImageField(upload_to='main/company_images/')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}) {self.company.name}"
    
    class Meta:
        verbose_name = "Изобрадения о компании"
        verbose_name_plural = "Изобрадении о компании" 


class SocialMedia(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()

    def __str__(self):
        return f"{self.pk}) {self.title}"
    
    class Meta:
        verbose_name = "Ссылка"     
        verbose_name_plural = "Ссылкы" 


class BestEmployees(models.Model):
    created_at = models.DateField(default=timezone.now)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk}) {self.employee.first_name}"
    
    class Meta:
        verbose_name = "Лучшие сотрудник"     
        verbose_name_plural = "Лучшие сотрудники " 
