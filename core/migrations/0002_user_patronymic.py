# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Отчество', null=True),
        ),
    ]
