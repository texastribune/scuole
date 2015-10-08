# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0023_auto_20151007_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='phone',
            field=models.CharField(default=0, max_length=10, verbose_name='District phone number'),
            preserve_default=False,
        ),
    ]
