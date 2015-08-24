# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0004_remove_regionstats_all_students_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Geographic name for region'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_id',
            field=models.CharField(max_length=2, verbose_name='Region identifier'),
        ),
    ]
