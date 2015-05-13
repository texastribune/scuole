# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0002_auto_20150512_1542'),
        ('districts', '0002_district_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='county',
            field=models.ForeignKey(related_name='districts', blank=True, to='counties.County', null=True),
        ),
    ]
