# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0025_auto_20151001_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='latitude',
            field=models.FloatField(verbose_name='District office latitude'),
        ),
        migrations.AlterField(
            model_name='district',
            name='longitude',
            field=models.FloatField(verbose_name='District office longitude'),
        ),
        migrations.AlterField(
            model_name='district',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
