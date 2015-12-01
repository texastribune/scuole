# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0043_campus_school_type_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='school_type_slug',
        ),
    ]
