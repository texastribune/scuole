# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0009_auto_20150824_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='campusstats',
            name='american_indian_count',
            field=models.FloatField(verbose_name='Number of American Indian students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='american_indian_percent',
            field=models.FloatField(verbose_name='Percent of American Indian students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='at_risk_count',
            field=models.IntegerField(verbose_name='Number of at risk students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='at_risk_percent',
            field=models.FloatField(verbose_name='Percent of at risk students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='early_childhood_education_count',
            field=models.IntegerField(verbose_name='Number of early childhood education students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='early_childhood_education_percent',
            field=models.FloatField(verbose_name='Percent of early childhood education students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='eighth_percent',
            field=models.FloatField(verbose_name='Percent of eighth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='eigth_count',
            field=models.IntegerField(verbose_name='Number of eigth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='eleventh_count',
            field=models.IntegerField(verbose_name='Number of eleventh grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='eleventh_percent',
            field=models.FloatField(verbose_name='Percent of eleventh grade students', null=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='fifth_count',
            field=models.IntegerField(verbose_name='Number of fifth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='fifth_percent',
            field=models.FloatField(verbose_name='Percent of fifth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='first_count',
            field=models.IntegerField(verbose_name='Number of first grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='first_percent',
            field=models.FloatField(verbose_name='Percent of first grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='fourth_count',
            field=models.IntegerField(verbose_name='Number of fourth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='fourth_percent',
            field=models.FloatField(verbose_name='Percent of fourth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='kindergarten_count',
            field=models.IntegerField(verbose_name='Number of kindergarten students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='kindergarten_percent',
            field=models.FloatField(verbose_name='Percent of kindergarten students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='ninth_count',
            field=models.IntegerField(verbose_name='Number of ninth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='ninth_percent',
            field=models.FloatField(verbose_name='Percent of ninth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='prek_count',
            field=models.IntegerField(verbose_name='Number of pre-K students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='prek_percent',
            field=models.FloatField(verbose_name='Percent of pre-K students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='second_count',
            field=models.IntegerField(verbose_name='Number of second grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='second_percent',
            field=models.FloatField(verbose_name='Percent of second grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='seventh_count',
            field=models.IntegerField(verbose_name='Number of seventh grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='seventh_percent',
            field=models.FloatField(verbose_name='Percent of seventh grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='sixth_count',
            field=models.IntegerField(verbose_name='Number of sixth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='sixth_percent',
            field=models.FloatField(verbose_name='Percent of sixth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='teacher_average_tenure',
            field=models.FloatField(verbose_name='Average tenure of teachers', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='teacher_student_radio',
            field=models.FloatField(verbose_name='Number of teachers per student', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='tenth_count',
            field=models.IntegerField(verbose_name='Number of tenth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='tenth_percent',
            field=models.FloatField(verbose_name='Percent of tenth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='third_count',
            field=models.IntegerField(verbose_name='Number of third grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='third_percent',
            field=models.FloatField(verbose_name='Percent of third grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='twelfth_count',
            field=models.IntegerField(verbose_name='Number of twelfth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='twelfth_percent',
            field=models.FloatField(verbose_name='Percent of twelfth grade students', null=True, blank=True),
        ),
    ]
