# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0028_auto_20151125_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regionstats',
            name='accountability_rating',
        ),
    ]
