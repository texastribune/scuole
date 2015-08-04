# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0003_auto_20150804_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regionstats',
            name='all_students_percent',
        ),
    ]
