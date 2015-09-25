# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0012_auto_20150922_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='statestats',
            name='bilingual_esl_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in bilingual/ESL program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='bilingual_esl_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in bilingual/ESL program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='career_technical_education_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in career and technical education program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='career_technical_education_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in career and technical education program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='gifted_and_talented_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in gifted and talented program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='gifted_and_talented_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in gifted and talented program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='special_education_count',
            field=models.IntegerField(blank=True, verbose_name='Number of students enrolled in special education program', null=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='special_education_percent',
            field=models.FloatField(blank=True, verbose_name='Percent of students enrolled in special education program', null=True),
        ),
    ]
