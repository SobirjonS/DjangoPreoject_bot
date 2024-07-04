# Generated by Django 5.0.6 on 2024-07-04 05:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('middle_name', models.CharField(default=True, max_length=255, null=True)),
                ('telegram', models.CharField(default=True, max_length=255, null=True)),
                ('birth_date', models.DateField(default=True, null=True)),
                ('started_work', models.DateField(default=True, null=True)),
                ('supervisor', models.CharField(max_length=255)),
                ('raiting', models.FloatField(default=True, null=True)),
                ('block', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='author_avatas/')),
                ('status', models.CharField(choices=[('менеджер по продажам', 'менеджер по продажам'), ('руководитель отдела продаж', 'руководитель отдела продаж'), ('руководитель группы', 'руководитель группы'), ('финансовый директор', 'финансовый директор'), ('директор по развитию', 'директор по развитию'), ('генеральный директор', 'генеральный директор'), ('учредитель', 'учредитель'), ('контроллер', 'контроллер')], default=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]