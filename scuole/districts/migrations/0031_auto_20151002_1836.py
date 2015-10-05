# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0030_auto_20151002_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='district',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='district',
            name='latlong',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
