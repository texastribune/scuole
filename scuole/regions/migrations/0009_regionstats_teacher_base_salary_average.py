# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0008_auto_20150922_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionstats',
            name='teacher_base_salary_average',
            field=models.IntegerField(verbose_name='Average teacher salary at entity', null=True, blank=True),
        ),
    ]
