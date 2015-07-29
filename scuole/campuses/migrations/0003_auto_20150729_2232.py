# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0002_auto_20150520_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'campuses'},
        ),
    ]
