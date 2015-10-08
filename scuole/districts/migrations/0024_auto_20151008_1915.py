# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0023_auto_20151007_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtstats',
            name='american_indian_count',
            field=models.IntegerField(null=True, verbose_name='Number of American Indian students', blank=True),
        ),
    ]
