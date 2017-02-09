# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_remove_aboutpage_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='about',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
    ]
