# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0024_commissioner'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='shape',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, verbose_name='State shape'),
        ),
    ]
