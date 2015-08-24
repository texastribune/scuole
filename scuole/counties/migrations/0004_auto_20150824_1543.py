# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0003_auto_20150729_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='fips',
            field=models.CharField(max_length=3, verbose_name='County FIPS place code'),
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=100, verbose_name='County name'),
        ),
    ]
