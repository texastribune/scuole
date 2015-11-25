# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0026_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionstats',
            name='accountabilityRating',
            field=models.CharField(max_length=30, null=True, verbose_name='Accountability rating', blank=True),
        ),
    ]
