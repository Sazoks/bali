# Generated by Django 3.2.9 on 2021-12-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectgallery',
            name='isVideo',
            field=models.BooleanField(default=False, verbose_name='Использовать видео?'),
        ),
        migrations.AddField(
            model_name='projectgallery',
            name='videoYouTube',
            field=models.URLField(default='', verbose_name='Видео для проекта'),
            preserve_default=False,
        ),
    ]
