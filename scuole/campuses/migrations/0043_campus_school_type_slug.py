# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0042_auto_20151125_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='school_type_slug',
            field=models.SlugField(default='elementary-school', max_length=40),
            preserve_default=False,
        ),
    ]
