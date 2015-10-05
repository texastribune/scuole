# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0025_auto_20151001_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='latlong',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
    ]
