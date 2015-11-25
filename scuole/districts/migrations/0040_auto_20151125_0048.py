# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0039_auto_20151124_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtstats',
            name='accountabilityRating',
        ),
        migrations.AddField(
            model_name='districtstats',
            name='accountability_rating',
            field=models.CharField(max_length=30, null=True, verbose_name='Accountability rating', blank=True),
        ),
    ]
