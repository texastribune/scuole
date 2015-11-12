# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0026_statestats_college_ready_graduates_math_limited_english_proficient_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_african_american_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of African American students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_african_american_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of African American students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_african_american_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of African American students taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_all_students_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of students who scored above criterion onat least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_all_students_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of students who scored above criterion onat least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_all_students_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of students taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_american_indian_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of American Insian students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_american_indian_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of American Insian students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_american_indian_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of American Insian students taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_asian_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of Asian students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_asian_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of Asian students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_asian_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of Asian students taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_economically_disadvantaged_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of white students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_economically_disadvantaged_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of economically disadvantaged students whoscored above criterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_economically_disadvantaged_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of economically disadvantaged students takingat least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_hispanic_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of Hispanic students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_hispanic_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of Hispanic students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_hispanic_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of Hispanic students taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_pacific_islander_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of Pacific Islander students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_pacific_islander_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of Pacific Islander students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_pacific_islander_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of Pacific Islander students taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_two_or_more_races_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of students of two or more races who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_two_or_more_races_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of students of two or more races who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_two_or_more_races_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of students of two or more races taking at least oneAP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_white_count_above_criterion',
            field=models.IntegerField(null=True, verbose_name='Number of white students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_white_percent_above_criterion',
            field=models.FloatField(null=True, verbose_name='Percent of white students who scored abovecriterion on at least one AP or IB test', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='ap_ib_white_percent_taking',
            field=models.FloatField(null=True, verbose_name='Percent of white students taking at least oneAP or IB test', blank=True),
        ),
    ]
