# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0016_auto_20150923_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtstats',
            name='bilingual_esl_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in bilingual/ESL program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='bilingual_esl_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in bilingual/ESL program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='career_technical_education_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in career and technical education program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='career_technical_education_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in career and technical education program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='gifted_and_talented_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in gifted and talented program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='gifted_and_talented_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in gifted and talented program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='special_education_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in special education program', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='special_education_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in special education program', null=True),
        ),
    ]
