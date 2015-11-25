# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0028_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='statestats',
            name='accountabilityRating',
            field=models.CharField(max_length=30, null=True, verbose_name='Accountability rating', blank=True),
        ),
    ]
