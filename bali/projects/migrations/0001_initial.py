# Generated by Django 3.2.9 on 2021-12-01 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название категории')),
                ('name_ru', models.TextField(null=True, verbose_name='Название категории')),
                ('name_en', models.TextField(null=True, verbose_name='Название категории')),
                ('name_ar', models.TextField(null=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название локации')),
                ('name_ru', models.TextField(null=True, verbose_name='Название локации')),
                ('name_en', models.TextField(null=True, verbose_name='Название локации')),
                ('name_ar', models.TextField(null=True, verbose_name='Название локации')),
            ],
            options={
                'verbose_name': 'Локация',
                'verbose_name_plural': 'Локации',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название проекта')),
                ('name_ru', models.TextField(null=True, verbose_name='Название проекта')),
                ('name_en', models.TextField(null=True, verbose_name='Название проекта')),
                ('name_ar', models.TextField(null=True, verbose_name='Название проекта')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('address_ru', models.TextField(null=True, verbose_name='Адрес')),
                ('address_en', models.TextField(null=True, verbose_name='Адрес')),
                ('address_ar', models.TextField(null=True, verbose_name='Адрес')),
                ('price', models.BigIntegerField(verbose_name='Стоимость проекта')),
                ('description', models.TextField(verbose_name='Описание проекта')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание проекта')),
                ('description_en', models.TextField(null=True, verbose_name='Описание проекта')),
                ('description_ar', models.TextField(null=True, verbose_name='Описание проекта')),
                ('area', models.SmallIntegerField(verbose_name='Площадь')),
                ('count_bedrooms', models.SmallIntegerField(verbose_name='Количество спален')),
                ('view', models.TextField(help_text='Открывающийся из виллы вид', verbose_name='Вид')),
                ('view_ru', models.TextField(help_text='Открывающийся из виллы вид', null=True, verbose_name='Вид')),
                ('view_en', models.TextField(help_text='Открывающийся из виллы вид', null=True, verbose_name='Вид')),
                ('view_ar', models.TextField(help_text='Открывающийся из виллы вид', null=True, verbose_name='Вид')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('invested', models.BooleanField(default=False, verbose_name='Проект подлежит инвестированию')),
                ('public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('main_image', models.ImageField(null=True, upload_to='sys/projects/', verbose_name='Главное изображение')),
                ('categories', models.ManyToManyField(related_name='projects', related_query_name='project', to='projects.Category', verbose_name='Категории')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', related_query_name='project', to='projects.location', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sys/projects/', verbose_name='Изображение для проекта')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.project')),
            ],
            options={
                'verbose_name': 'Галерея проекта',
                'verbose_name_plural': 'Галереи проектов',
            },
        ),
        migrations.CreateModel(
            name='LocationFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Заголовок факта')),
                ('title_ru', models.TextField(null=True, verbose_name='Заголовок факта')),
                ('title_en', models.TextField(null=True, verbose_name='Заголовок факта')),
                ('title_ar', models.TextField(null=True, verbose_name='Заголовок факта')),
                ('description', models.TextField(verbose_name='Описание факта')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание факта')),
                ('description_en', models.TextField(null=True, verbose_name='Описание факта')),
                ('description_ar', models.TextField(null=True, verbose_name='Описание факта')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facts', related_query_name='fact', to='projects.location', verbose_name='Локация')),
            ],
            options={
                'verbose_name': 'Факт о локации',
                'verbose_name_plural': 'Факты о локациях',
            },
        ),
        migrations.CreateModel(
            name='AdvantagesProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название преимущества')),
                ('name_ru', models.TextField(null=True, verbose_name='Название преимущества')),
                ('name_en', models.TextField(null=True, verbose_name='Название преимущества')),
                ('name_ar', models.TextField(null=True, verbose_name='Название преимущества')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advantages', related_query_name='advantage', to='projects.project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Преимущество проекта',
                'verbose_name_plural': 'Преимущества проектов',
            },
        ),
    ]
