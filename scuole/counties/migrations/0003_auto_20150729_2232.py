# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0002_auto_20150512_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'counties'},
        ),
    ]
