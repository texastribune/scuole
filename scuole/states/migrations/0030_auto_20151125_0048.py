# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0029_statestats_accountabilityrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statestats',
            old_name='accountabilityRating',
            new_name='accountability_rating',
        ),
    ]
