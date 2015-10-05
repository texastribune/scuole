# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0032_auto_20151002_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True),
        ),
    ]
