# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0027_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='districtstats',
            old_name='teacher_average_experience',
            new_name='teacher_avg_experience',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='teacher_average_tenure',
            new_name='teacher_avg_tenure',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='teacher_base_salary_average',
            new_name='teacher_base_salary_avg',
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_beginning_salary_avg',
            field=models.DecimalField(null=True, verbose_name='Average teacher beginning salary at entity', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_eleven_thru_twenty_salary_avg',
            field=models.DecimalField(null=True, verbose_name='Average salary for teachers with 11-20 years experience', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_one_thru_five_salary_avg',
            field=models.DecimalField(null=True, verbose_name='Average salary for teachers with 1-5 years experience', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_over_twenty_salary',
            field=models.DecimalField(null=True, verbose_name='Average salary for teachers with over 20 years experience', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='districtstats',
            name='teacher_six_thru_ten_salary_avg',
            field=models.DecimalField(null=True, verbose_name='Average salary for teachers with 6-10 years experience', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='districtstats',
            name='dropout_at_risk_count',
            field=models.IntegerField(null=True, verbose_name='Number of 9-12 white students who dropped out', blank=True),
        ),
    ]
