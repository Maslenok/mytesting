# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_remove_answer_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='Ответ правильный'),
        ),
    ]
