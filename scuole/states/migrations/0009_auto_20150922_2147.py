# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0008_auto_20150922_2142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statestats',
            old_name='eigth_count',
            new_name='eighth_count',
        ),
    ]
