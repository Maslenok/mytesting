# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0005_auto_20170224_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='position',
        ),
        migrations.RemoveField(
            model_name='question',
            name='position',
        ),
    ]