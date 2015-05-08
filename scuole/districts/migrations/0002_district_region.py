# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(related_name='districts', blank=True, to='regions.Region', null=True),
        ),
    ]
