# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0010_auto_20150922_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='statestats',
            name='teacher_base_salary_average',
            field=models.IntegerField(verbose_name='Average teacher salary at entity', null=True, blank=True),
        ),
    ]
