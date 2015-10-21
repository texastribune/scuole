# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0028_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campusstats',
            old_name='teacher_eleven_thru_twenty_salary_avg',
            new_name='teacher_avg_11_to_20_year_salary',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='teacher_one_thru_five_salary_avg',
            new_name='teacher_avg_1_to_5_year_salary',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='teacher_over_twenty_salary',
            new_name='teacher_avg_20_plus_year_salary',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='teacher_six_thru_ten_salary_avg',
            new_name='teacher_avg_6_to_10_year_salary',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='teacher_base_salary_avg',
            new_name='teacher_avg_base_salary',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='teacher_beginning_salary_avg',
            new_name='teacher_avg_beginning_salary',
        ),
    ]
