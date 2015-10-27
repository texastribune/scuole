# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0031_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_african_american_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of African American students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_african_american_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of African American students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_all_students_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of all students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_all_students_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of all students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_american_indian_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of American Indian students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_american_indian_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of American Indian students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_asian_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of asian students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_asian_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of asian students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_at_risk_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of at risk students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_at_risk_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of at risk students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_economically_disadvantaged_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of economically disadvantaged students who met STAAR level 2 phase-in', db_column='staar_all_subjects_econ_disadv_met_level_two_count', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_economically_disadvantaged_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of economically disadvantaged students who met STAAR level 2 phase-in', db_column='staar_all_subjects_econ_disadv_met_level_two_percent', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_hispanic_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of Hispanic students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_hispanic_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of Hispanic students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_pacific_islander_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of Pacific Islander students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_pacific_islander_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of Pacific Islander students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_two_or_more_races_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of students of two or more races who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_two_or_more_races_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of students of two or more races who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_white_met_level_two_count',
            field=models.IntegerField(null=True, verbose_name='Number of white students who met STAAR level 2 phase-in', blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='staar_all_subjects_white_met_level_two_percent',
            field=models.FloatField(null=True, verbose_name='Percent of white students who met STAAR level 2 phase-in', blank=True),
        ),
    ]
