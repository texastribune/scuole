# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0027_auto_20151002_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
