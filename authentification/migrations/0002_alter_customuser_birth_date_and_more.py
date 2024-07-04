# Generated by Django 5.0.6 on 2024-07-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='raiting',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='started_work',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(blank=True, choices=[('менеджер по продажам', 'менеджер по продажам'), ('руководитель отдела продаж', 'руководитель отдела продаж'), ('руководитель группы', 'руководитель группы'), ('финансовый директор', 'финансовый директор'), ('директор по развитию', 'директор по развитию'), ('генеральный директор', 'генеральный директор'), ('учредитель', 'учредитель'), ('контроллер', 'контроллер')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='supervisor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]