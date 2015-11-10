# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0021_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_limited_english_proficient_count',
            field=models.IntegerField(null=True, verbose_name='Number of college ready limited english proficient graduates in both subjects', db_column='college_ready_graduates_both_lep_count', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_both_limited_english_proficient_percent',
            field=models.FloatField(null=True, verbose_name='Percent of college ready limited english proficient graduates in both subjects', db_column='college_ready_graduates_both_lep_percent', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_limited_english_proficient_count',
            field=models.IntegerField(null=True, verbose_name='Number of college ready limited english proficient graduates in English', db_column='college_ready_graduates_english_lep_count', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_english_limited_english_proficient_percent',
            field=models.FloatField(null=True, verbose_name='Percent of college ready limited english proficient graduates in English', db_column='college_ready_graduates_english_lep_percent', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='college_ready_graduates_math_limited_english_proficient_percent',
            field=models.FloatField(null=True, verbose_name='Percent of college ready limited english proficient graduates in math', db_column='college_ready_graduates_math_lep_percent', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_limited_english_proficient_count',
            field=models.IntegerField(null=True, verbose_name='Number of 9-12 limited English proficient students who dropped out', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='dropout_limited_english_proficient_percent',
            field=models.FloatField(null=True, verbose_name='Percent of 9-12 limited English proficient students who dropped out', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_limted_english_proficient_count',
            field=models.IntegerField(null=True, verbose_name='Number of limited English proficient students who graduated in 4 years', blank=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_limted_english_proficient_percent',
            field=models.FloatField(null=True, verbose_name='Percent of limited English proficient students who graduated in 4 years', blank=True),
        ),
    ]