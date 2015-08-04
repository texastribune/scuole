# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0006_auto_20150804_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtstats',
            name='all_students_percent',
        ),
    ]
