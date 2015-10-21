# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0028_campus_phone_number_extension'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campus',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
