# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0022_auto_20151028_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regionstats',
            old_name='four_year_graduate_limted_english_proficient_count',
            new_name='four_year_graduate_limited_english_proficient_count',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='four_year_graduate_limted_english_proficient_percent',
            new_name='four_year_graduate_limited_english_proficient_percent',
        ),
    ]
