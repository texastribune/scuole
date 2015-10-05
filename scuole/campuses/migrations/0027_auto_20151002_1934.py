# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0026_auto_20151002_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='latlong',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]
