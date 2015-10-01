# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0021_auto_20150929_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='latitude',
            field=models.FloatField(verbose_name='Campus latitude'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='longitude',
            field=models.FloatField(verbose_name='District office longitude'),
        ),
    ]
