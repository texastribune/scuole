# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0004_auto_20150730_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='districtstats',
            options={'verbose_name_plural': 'District stats'},
        ),
    ]
