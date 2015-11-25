# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0040_campusstats_accountabilityrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campusstats',
            old_name='accountabilityRating',
            new_name='accountability_rating',
        ),
    ]
