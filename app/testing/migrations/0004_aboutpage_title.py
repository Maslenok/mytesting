# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_auto_20170209_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='title',
            field=models.CharField(help_text='О нас', default=1, max_length=100),
            preserve_default=False,
        ),
    ]
