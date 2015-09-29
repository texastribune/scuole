# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0017_auto_20150928_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statestats',
            name='avg_act_score_american_indian',
            field=models.FloatField(null=True, verbose_name=b'Average ACT score for American Indian students', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='avg_sat_score_american_indian',
            field=models.IntegerField(null=True, verbose_name=b'Average SAT score for American Indian students', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='college_ready_graduates_both_american_indian_count',
            field=models.IntegerField(null=True, verbose_name=b'Number of college ready American Indian graduates in both subjects', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='college_ready_graduates_both_american_indian_percent',
            field=models.FloatField(null=True, verbose_name=b'Percent of college ready American Indian graduates in both subjects', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='college_ready_graduates_english_american_indian_count',
            field=models.IntegerField(null=True, verbose_name=b'Number of college ready American Indian graduates in English', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='college_ready_graduates_english_american_indian_percent',
            field=models.FloatField(null=True, verbose_name=b'Percent of college ready American Indian graduates in english', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='college_ready_graduates_math_american_indian_count',
            field=models.IntegerField(null=True, verbose_name=b'Number of college ready American Indian graduates in math', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='college_ready_graduates_math_american_indian_percent',
            field=models.FloatField(null=True, verbose_name=b'Percent of college ready American Indian graduates in math', blank=True),
        ),
    ]
