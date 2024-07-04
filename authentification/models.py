from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    started_work = models.DateField(null=True, blank=True)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    raiting = models.FloatField(null=True, blank=True)
    block = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='author_avatas/', null=True, blank=True)
    STATUS_CHOICES = (
        ('менеджер по продажам', 'менеджер по продажам'),
        ('руководитель отдела продаж', 'руководитель отдела продаж'),
        ('руководитель группы', 'руководитель группы'),
        ('финансовый директор', 'финансовый директор'),
        ('директор по развитию', 'директор по развитию'),
        ('генеральный директор', 'генеральный директор'),
        ('учредитель', 'учредитель'),
        ('контроллер', 'контроллер')
    )

    job = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        null=True, blank=True
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"  