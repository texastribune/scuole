# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0040_auto_20151125_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='accountability_rating',
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='accountability_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue')], verbose_name='Accountability rating', default='', max_length=1),
        ),
    ]
