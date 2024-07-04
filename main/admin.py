from django.contrib import admin
from django.apps import AppConfig
from . import models


admin.site.register(models.Category)
admin.site.register(models.News)
admin.site.register(models.NewsImage)
admin.site.register(models.Lesson)
admin.site.register(models.LessonsImage)
admin.site.register(models.LessonsVideo)
admin.site.register(models.Test)
admin.site.register(models.Evaluation)
admin.site.register(models.File)
admin.site.register(models.Programm)
admin.site.register(models.ProgrammsImage)
admin.site.register(models.Prize)
admin.site.register(models.Fine)
admin.site.register(models.Error)
admin.site.register(models.Company)
admin.site.register(models.SocialMedia)
admin.site.register(models.BestEmployees)

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals