# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0011_auto_20150922_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campusstats',
            name='teacher_student_radio',
        ),
        migrations.AddField(
            model_name='campusstats',
            name='students_per_teacher',
            field=models.FloatField(verbose_name='Number of students per teacher', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='teacher_average_experience',
            field=models.FloatField(verbose_name='Average years of experience at entity', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campusstats',
            name='teacher_average_tenure',
            field=models.FloatField(verbose_name='Average tenure of teachers at entity', blank=True, null=True),
        ),
    ]
