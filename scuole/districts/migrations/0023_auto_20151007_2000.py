# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0022_auto_20150929_1636'),
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
        migrations.AddField(
            model_name='district',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(null=True, verbose_name='District office coordinates', srid=4326),
        ),
        migrations.AddField(
            model_name='district',
            name='shape',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, verbose_name='District shape', srid=4326),
        ),
    ]
