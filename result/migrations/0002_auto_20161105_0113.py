# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-04 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersanswer',
            name='answers_list',
            field=models.TextField(),
        ),
    ]
