# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='desc',
        ),
    ]