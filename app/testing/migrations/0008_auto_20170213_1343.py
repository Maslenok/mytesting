# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0007_aboutpage_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='title',
            field=models.CharField(help_text='О нас', max_length=100, verbose_name='Заголовок'),
        ),
    ]
