# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0022_auto_20151007_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='accountability_rating',
            field=models.CharField(default='N/A', max_length=3, verbose_name='Accountability rating', choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X/Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue')]),
            preserve_default=False,
        ),
    ]