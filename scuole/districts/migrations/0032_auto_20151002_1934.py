# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0031_auto_20151002_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='latitude',
            field=models.FloatField(verbose_name='District office latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='longitude',
            field=models.FloatField(verbose_name='District office longitude'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
