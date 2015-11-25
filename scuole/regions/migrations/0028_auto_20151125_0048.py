# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0027_regionstats_accountabilityrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regionstats',
            old_name='accountabilityRating',
            new_name='accountability_rating',
        ),
    ]
