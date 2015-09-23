# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0011_auto_20150922_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='districtstats',
            old_name='eigth_count',
            new_name='eighth_count',
        ),
    ]
