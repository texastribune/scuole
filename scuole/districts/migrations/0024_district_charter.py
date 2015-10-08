# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0023_auto_20151007_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='charter',
            field=models.BooleanField(default='A', verbose_name='District charter operator', choices=[(('Y',), True), (('N',), False)]),
            preserve_default=False,
        ),
    ]
