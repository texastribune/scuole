# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0026_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(max_length=20, verbose_name='Campus phone number'),
        ),
        migrations.AlterField(
            model_name='campusstats',
            name='dropout_at_risk_count',
            field=models.IntegerField(null=True, verbose_name='Number of 9-12 white students who dropped out', blank=True),
        ),
    ]
