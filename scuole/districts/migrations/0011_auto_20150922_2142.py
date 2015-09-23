# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0010_auto_20150824_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='districtstats',
            name='american_indian_count',
            field=models.FloatField(verbose_name='Number of American Indian students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='american_indian_percent',
            field=models.FloatField(verbose_name='Percent of American Indian students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='at_risk_count',
            field=models.IntegerField(verbose_name='Number of at risk students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='at_risk_percent',
            field=models.FloatField(verbose_name='Percent of at risk students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='early_childhood_education_count',
            field=models.IntegerField(verbose_name='Number of early childhood education students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='early_childhood_education_percent',
            field=models.FloatField(verbose_name='Percent of early childhood education students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='eighth_percent',
            field=models.FloatField(verbose_name='Percent of eighth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='eigth_count',
            field=models.IntegerField(verbose_name='Number of eigth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='eleventh_count',
            field=models.IntegerField(verbose_name='Number of eleventh grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='eleventh_percent',
            field=models.FloatField(verbose_name='Percent of eleventh grade students', null=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='fifth_count',
            field=models.IntegerField(verbose_name='Number of fifth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='fifth_percent',
            field=models.FloatField(verbose_name='Percent of fifth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='first_count',
            field=models.IntegerField(verbose_name='Number of first grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='first_percent',
            field=models.FloatField(verbose_name='Percent of first grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='fourth_count',
            field=models.IntegerField(verbose_name='Number of fourth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='fourth_percent',
            field=models.FloatField(verbose_name='Percent of fourth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='kindergarten_count',
            field=models.IntegerField(verbose_name='Number of kindergarten students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='kindergarten_percent',
            field=models.FloatField(verbose_name='Percent of kindergarten students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='ninth_count',
            field=models.IntegerField(verbose_name='Number of ninth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='ninth_percent',
            field=models.FloatField(verbose_name='Percent of ninth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='prek_count',
            field=models.IntegerField(verbose_name='Number of pre-K students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='prek_percent',
            field=models.FloatField(verbose_name='Percent of pre-K students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='second_count',
            field=models.IntegerField(verbose_name='Number of second grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='second_percent',
            field=models.FloatField(verbose_name='Percent of second grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='seventh_count',
            field=models.IntegerField(verbose_name='Number of seventh grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='seventh_percent',
            field=models.FloatField(verbose_name='Percent of seventh grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='sixth_count',
            field=models.IntegerField(verbose_name='Number of sixth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='sixth_percent',
            field=models.FloatField(verbose_name='Percent of sixth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_average_tenure',
            field=models.FloatField(verbose_name='Average tenure of teachers', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_student_radio',
            field=models.FloatField(verbose_name='Number of teachers per student', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='tenth_count',
            field=models.IntegerField(verbose_name='Number of tenth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='tenth_percent',
            field=models.FloatField(verbose_name='Percent of tenth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='third_count',
            field=models.IntegerField(verbose_name='Number of third grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='third_percent',
            field=models.FloatField(verbose_name='Percent of third grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='twelfth_count',
            field=models.IntegerField(verbose_name='Number of twelfth grade students', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='twelfth_percent',
            field=models.FloatField(verbose_name='Percent of twelfth grade students', null=True, blank=True),
        ),
    ]
