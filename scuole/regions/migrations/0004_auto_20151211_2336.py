# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0003_auto_20151211_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_african_american_percent',
            new_name='teacher_african_american_fte_percent',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_american_indian_percent',
            new_name='teacher_american_indian_fte_percent',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_asian_percent',
            new_name='teacher_asian_fte_percent',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_hispanic_percent',
            new_name='teacher_hispanic_fte_percent',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_pacific_islander_percent',
            new_name='teacher_pacific_islander_fte_percent',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_two_or_more_races_percent',
            new_name='teacher_two_or_more_races_fte_percent',
        ),
        migrations.RenameField(
            model_name='regionstats',
            old_name='teacher_white_percent',
            new_name='teacher_white_fte_percent',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_african_american_count',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_american_indian_count',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_asian_count',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_hispanic_count',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_pacific_islander_count',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_two_or_more_races_count',
        ),
        migrations.RemoveField(
            model_name='regionstats',
            name='teacher_white_count',
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_african_american_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of African American teachers'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_american_indian_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of American Indian teachers'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_asian_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of Asian teachers'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_hispanic_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of Hispanic teachers'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_pacific_islander_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of Pacific Islander teachers'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_two_or_more_races_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of teachers of two or more races'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='teacher_white_fte_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of white teachers'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='teacher_bachelors_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of teachers with bachelors degree'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='teacher_doctorate_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of teachers with doctorate degree'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='teacher_masters_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of teachers with masters degree'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='teacher_no_degree_count',
            field=models.FloatField(blank=True, null=True, verbose_name='Number of teachers with no degree'),
        ),
    ]
