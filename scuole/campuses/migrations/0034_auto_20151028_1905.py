# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0033_auto_20151028_1847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campusstats',
            old_name='four_year_graduate_limted_english_proficient_count',
            new_name='four_year_graduate_limited_english_proficient_count',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='four_year_graduate_limted_english_proficient_percent',
            new_name='four_year_graduate_limited_english_proficient_percent',
        ),
    ]
