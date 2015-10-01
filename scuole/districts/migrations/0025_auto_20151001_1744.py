# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0024_auto_20151001_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='District office latitude'),
        ),
        migrations.AlterField(
            model_name='district',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='District office longitude'),
        ),
    ]
