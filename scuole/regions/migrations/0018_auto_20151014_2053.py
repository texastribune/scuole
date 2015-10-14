# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0017_auto_20151008_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionstats',
            name='dropout_at_risk_count',
            field=models.IntegerField(null=True, verbose_name='Number of 9-12 white students who dropped out', blank=True),
        ),
    ]
