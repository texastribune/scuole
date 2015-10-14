# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0024_district_accountability_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='accountability_rating',
            field=models.CharField(max_length=4, verbose_name='Accountability rating', choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue')]),
        ),
    ]
