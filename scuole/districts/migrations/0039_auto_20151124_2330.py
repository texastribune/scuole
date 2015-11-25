# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0038_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtstats',
            name='accountabilityRating',
            field=models.CharField(max_length=30, null=True, verbose_name='Accountability rating', blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='accountability_rating',
            field=models.CharField(max_length=1, verbose_name='Accountability rating', choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue')]),
        ),
    ]
