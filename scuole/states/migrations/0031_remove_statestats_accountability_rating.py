# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0030_auto_20151125_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statestats',
            name='accountability_rating',
        ),
    ]
