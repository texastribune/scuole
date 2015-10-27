# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0024_auto_20151023_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_african_american_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_african_american_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_all_students_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_all_students_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_american_indian_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_american_indian_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_asian_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_asian_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_at_risk_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_at_risk_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_economically_disadvantaged_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_economically_disadvantaged_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_hispanic_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_hispanic_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_pacific_islander_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_pacific_islander_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_two_or_more_races_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_two_or_more_races_met_level_two_percent',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_white_met_level_two_count',
        ),
        migrations.RemoveField(
            model_name='statestats',
            name='staar_all_subjects_white_met_level_two_percent',
        ),
    ]
