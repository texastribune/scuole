# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0023_auto_20151001_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Campus latitude'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Campus longitude'),
        ),
    ]
