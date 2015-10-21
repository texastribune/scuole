# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0017_auto_20151008_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_african_american_count',
            field=models.IntegerField(blank=True, verbose_name='Number of African American students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_african_american_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of African American students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_all_students_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_all_students_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_american_indian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of American Indian students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_american_indian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of American Indian students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_asian_count',
            field=models.IntegerField(blank=True, verbose_name='Number of Asian students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_asian_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of Asian students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_at_risk_count',
            field=models.IntegerField(blank=True, verbose_name='Number of at risk students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_at_risk_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of at risk students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_economically_disadvantaged_count',
            field=models.IntegerField(blank=True, verbose_name='Number of economically disadvantaged students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_economically_disadvantaged_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of economically disadvantaged students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_hispanic_count',
            field=models.IntegerField(blank=True, verbose_name='Number of Hispanic students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_hispanic_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of Hispanic students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_pacific_islander_count',
            field=models.IntegerField(blank=True, verbose_name='Number of Pacific Islander students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_pacific_islander_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of Pacific Islander students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_two_or_more_races_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students of two or more races who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_two_or_more_races_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students of two or more races who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_white_count',
            field=models.IntegerField(blank=True, verbose_name='Number of white students who graduated in 4 years', null=True),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='four_year_graduate_white_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of white students who graduated in 4 years', null=True),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='dropout_at_risk_count',
            field=models.IntegerField(blank=True, verbose_name='Number of 9-12 white students who dropped out', null=True),
        ),
    ]
