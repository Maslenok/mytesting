# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing_code', '0004_answer_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='course',
        ),
    ]