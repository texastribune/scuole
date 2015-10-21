# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0027_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtstats',
            name='dropout_at_risk_count',
            field=models.IntegerField(null=True, verbose_name='Number of 9-12 white students who dropped out', blank=True),
        ),
    ]
