# Generated by Django 4.2.4 on 2023-09-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='ссылка на видео'),
        ),
    ]
