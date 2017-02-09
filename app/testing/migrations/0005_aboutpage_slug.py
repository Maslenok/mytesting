# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_aboutpage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='slug',
            field=models.SlugField(verbose_name='url', blank=True, max_length=100),
        ),
    ]
