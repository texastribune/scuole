# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-11 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0002_auto_20151208_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtstats',
            name='teacher_african_american_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of African American teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_african_american_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of African American teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_american_indian_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of American Indian teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_american_indian_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of American Indian teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_asian_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Asian teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_asian_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of Asian teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_bachelors_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teachers with bachelors degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_bachelors_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of teachers with bachelors degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_doctorate_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teachers with doctorate degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_doctorate_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of teachers with doctorate degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_hispanic_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Hispanic teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_hispanic_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of Hispanic teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_masters_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teachers with masters degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_masters_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of teachers with masters degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_no_degree_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teachers with no degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_no_degree_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of teachers with no degree'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_pacific_islander_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Pacific Islander teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_pacific_islander_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of Pacific Islander teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_two_or_more_races_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of teachers of two or more races'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_two_or_more_races_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of teachers of two or more races'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_white_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of white teachers'),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_white_percent',
            field=models.FloatField(blank=True, null=True, verbose_name='Percent of white teachers'),
        ),
    ]
