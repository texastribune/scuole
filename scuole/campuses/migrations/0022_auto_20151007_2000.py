# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0021_auto_20150929_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='campus',
            name='longitude',
        ),
        migrations.AddField(
            model_name='campus',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
