# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0003_auto_20150730_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtstats',
            name='african_american_count',
            field=models.IntegerField(default=0, verbose_name='Number of African American students'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='districtstats',
            name='two_or_more_races_count',
            field=models.IntegerField(default=0, verbose_name='Number of Two or More Races students'),
            preserve_default=False,
        ),
    ]
