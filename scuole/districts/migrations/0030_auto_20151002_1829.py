# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0029_auto_20151002_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='latlong',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
    ]
