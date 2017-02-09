# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(verbose_name='email address', max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30, default='', null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, default='', null=True, verbose_name='last name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Подпись')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, upload_to=core.models.get_photo_image_path, null=True, verbose_name='Аватар')),
                ('groups', models.ManyToManyField(blank=True, related_name='user_set', to='auth.Group', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_set', to='auth.Permission', related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-date_joined'],
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail для приёма заявок')),
                ('top_js', models.TextField(blank=True, verbose_name='Скрипты в <HEAD>..</HEAD>')),
                ('bottom_js', models.TextField(blank=True, verbose_name='Скрипты перед закрывающим </BODY>')),
                ('robots_txt', models.TextField(blank=True, null=True, verbose_name='robots.txt')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
    ]
