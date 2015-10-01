# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0022_auto_20151001_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='latlong',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campus',
            name='latitude',
            field=models.FloatField(verbose_name='Campus latitude'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='longitude',
            field=models.FloatField(verbose_name='Campus longitude'),
        ),
    ]
