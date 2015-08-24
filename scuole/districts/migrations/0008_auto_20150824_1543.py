# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0007_remove_districtstats_all_students_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.CharField(max_length=100, verbose_name='District office city'),
        ),
        migrations.AlterField(
            model_name='district',
            name='latitude',
            field=models.FloatField(verbose_name='District office latitude'),
        ),
        migrations.AlterField(
            model_name='district',
            name='longitude',
            field=models.FloatField(verbose_name='District office longitude'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=200, verbose_name='District name'),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.CharField(max_length=2, verbose_name='District office abbreviated state location'),
        ),
        migrations.AlterField(
            model_name='district',
            name='street',
            field=models.CharField(max_length=200, verbose_name='District street'),
        ),
        migrations.AlterField(
            model_name='district',
            name='tea_id',
            field=models.CharField(max_length=6, verbose_name='TEA district identifier'),
        ),
        migrations.AlterField(
            model_name='district',
            name='zip_code',
            field=models.CharField(max_length=5, verbose_name='District office ZIP Code'),
        ),
        migrations.AlterField(
            model_name='district',
            name='zip_code4',
            field=models.CharField(max_length=4, verbose_name='District office +4 ZIP Code'),
        ),
    ]
