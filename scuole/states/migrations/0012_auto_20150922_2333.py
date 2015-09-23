# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0011_statestats_teacher_base_salary_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statestats',
            name='teacher_base_salary_average',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name='Average teacher salary at entity', null=True),
        ),
    ]
