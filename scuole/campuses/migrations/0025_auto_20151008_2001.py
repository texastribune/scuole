# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0024_auto_20151008_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='charter',
            field=models.BooleanField(verbose_name='Campus charter status'),
        ),
    ]
