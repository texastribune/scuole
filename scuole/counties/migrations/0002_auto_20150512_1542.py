# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='fips',
            field=models.CharField(help_text='County FIPS place code', max_length=3),
        ),
    ]
