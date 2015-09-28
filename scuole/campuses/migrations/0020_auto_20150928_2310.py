# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0019_auto_20150928_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campusstats',
            old_name='avg_act_score_econ_disadv',
            new_name='avg_act_score_economically_disadvantaged',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='avg_sat_score_econ_disadv',
            new_name='avg_sat_score_economically_disadvantaged',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='dropout_econ_disadv_count',
            new_name='dropout_economically_disadvantaged_count',
        ),
        migrations.RenameField(
            model_name='campusstats',
            old_name='dropout_econ_disadv_percent',
            new_name='dropout_economically_disadvantaged_percent',
        ),
        migrations.RemoveField(
            model_name='campusstats',
            name='college_ready_graduates_both_econ_disadv_count',
        ),
        migrations.RemoveField(
            model_name='campusstats',
            name='college_ready_graduates_both_econ_disadv_percent',
        ),
        migrations.RemoveField(
            model_name='campusstats',
            name='college_ready_graduates_english_econ_disadv_count',
        ),
        migrations.RemoveField(
            model_name='campusstats',
            name='college_ready_graduates_english_econ_disadv_percent',
        ),
        migrations.RemoveField(
            model_name='campusstats',
            name='college_ready_graduates_math_econ_disadv_count',
        ),
        migrations.RemoveField(
            model_name='campusstats',
            name='college_ready_graduates_math_econ_disadv_percent',
        ),
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_both_economically_disadvantaged_count',
            field=models.IntegerField(null=True, verbose_name=b'Number of college ready economically disadvantaged graduates in both subjects', db_column=b'college_ready_graduates_both_econ_disadv_count', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_both_economically_disadvantaged_percent',
            field=models.FloatField(null=True, verbose_name=b'Percent of college ready economically disadvantaged graduates in both subjects', db_column=b'college_ready_graduates_both_econ_disadv_percent', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_english_economically_disadvantaged_count',
            field=models.IntegerField(null=True, verbose_name=b'Number of college ready economically disadvantaged graduates in English', db_column=b'college_ready_graduates_english_econ_disadv_count', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_english_economically_disadvantaged_percent',
            field=models.FloatField(null=True, verbose_name=b'Percent of college ready economically disadvantaged graduates in English', db_column=b'college_ready_graduates_english_econ_disadv_percent', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_math_economically_disadvantaged_count',
            field=models.IntegerField(null=True, verbose_name=b'Number of college ready economically disadvantaged graduates in math', db_column=b'college_ready_graduates_math_econ_disadv_count', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_math_economically_disadvantaged_percent',
            field=models.FloatField(null=True, verbose_name=b'Percent of college ready economically disadvantaged graduates in math', db_column=b'college_ready_graduates_math_econ_disadv_percent', blank=True),
        ),
    ]
