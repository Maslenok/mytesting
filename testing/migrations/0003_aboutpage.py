# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20170117_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='О нас')),
                ('is_active', models.BooleanField(default=False, verbose_name='Отоброжаемая страница')),
            ],
            options={
                'verbose_name_plural': 'О нас',
                'verbose_name': 'О нас',
                'db_table': 'about',
            },
        ),
    ]