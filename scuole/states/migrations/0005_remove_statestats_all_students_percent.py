# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0004_auto_20150804_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statestats',
            name='all_students_percent',
        ),
    ]
