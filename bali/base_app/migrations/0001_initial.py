# Generated by Django 3.2.9 on 2021-12-01 04:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=32, verbose_name='Номер телефона телефона')),
                ('date_submission', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
            ],
            options={
                'verbose_name': 'Данные для консультации',
                'verbose_name_plural': 'Данные для консультации',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('question_ru', models.TextField(null=True, verbose_name='Вопрос')),
                ('question_en', models.TextField(null=True, verbose_name='Вопрос')),
                ('question_ar', models.TextField(null=True, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ на вопрос')),
                ('answer_ru', models.TextField(null=True, verbose_name='Ответ на вопрос')),
                ('answer_en', models.TextField(null=True, verbose_name='Ответ на вопрос')),
                ('answer_ar', models.TextField(null=True, verbose_name='Ответ на вопрос')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=64, verbose_name='Имя клиента')),
                ('client_phone', models.CharField(max_length=32, verbose_name='Номер телефона клиента')),
                ('order_type', models.CharField(choices=[('R', 'Аренда вилл'), ('C', 'Строительство')], max_length=8, verbose_name='Тип заказа')),
                ('distance_to_sea', models.CharField(blank=True, choices=[('M5', '5 минут'), ('M10', '10 минут'), ('M15', 'от 15 минут')], max_length=8, null=True, verbose_name='Расстояние до моря')),
                ('profit_assessment', models.SmallIntegerField(blank=True, error_messages={'max_value': 'Максимальный оценка: 5', 'min_value': 'Минимальный оценка: 1'}, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Важность доходности')),
                ('assessment_district', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Важность района')),
                ('assessment_distance_to_sea', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Важность расстояния до моря')),
                ('rental_period', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(30)], verbose_name='Срок аренды')),
                ('budget', models.CharField(blank=True, choices=[('B1', 'от $300.000'), ('B2', '$200.000 - $500.000'), ('B3', '$500.000 - $1.000.000'), ('B4', '$1.000.000 - $3.000.000'), ('B5', 'Более $3.000.000')], max_length=8, null=True, verbose_name='Планируемый бюджет')),
                ('villa_area', models.CharField(blank=True, choices=[('R1', '1 спальня'), ('R2', '2 спальни'), ('R3', '3 спальни'), ('R4', '4 спальни и больше')], max_length=8, null=True, verbose_name='Площадь виллы')),
            ],
            options={
                'verbose_name': 'Квиз',
                'verbose_name_plural': 'Квизы',
            },
        ),
    ]
