# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0005_aboutpage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='slug',
        ),
    ]
