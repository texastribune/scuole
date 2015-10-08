# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0022_auto_20151007_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='charter',
            field=models.BooleanField(default='A', verbose_name='Campus charter status', choices=[(('Y',), True), (('N',), False)]),
            preserve_default=False,
        ),
    ]
