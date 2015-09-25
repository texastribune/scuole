# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0015_auto_20150922_2333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['name']},
        ),
    ]
