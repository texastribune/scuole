# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0024_district_charter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='charter',
            field=models.BooleanField(verbose_name='District charter operator', choices=[('Y', True), ('N', False)]),
        ),
    ]
