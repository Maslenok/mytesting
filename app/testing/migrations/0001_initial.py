# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('about', models.TextField(verbose_name='О нас')),
                ('is_active', models.BooleanField(verbose_name='Отоброжаемый текс', default=False)),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
                'db_table': 'about',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('answerText', models.TextField(verbose_name='Текст ответа')),
                ('is_correct', models.BooleanField(verbose_name='Ответ правильный', default=False)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('courseName', models.CharField(verbose_name='Название курса', max_length=255)),
                ('slug', models.SlugField(verbose_name='Отображение в UrL')),
                ('about', models.TextField(verbose_name='Описание курса ', blank=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('questionText', models.TextField(verbose_name='Вопрос')),
                ('curse', models.ForeignKey(verbose_name='Курс', to='testing.Course')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'db_table': 'questions',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='Относиться к вопросу', to='testing.Question'),
        ),
    ]
