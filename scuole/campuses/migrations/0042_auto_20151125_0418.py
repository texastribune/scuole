# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0041_auto_20151125_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='accountability_rating',
        ),
        migrations.AlterField(
            model_name='campus',
            name='high_grade',
            field=models.CharField(choices=[('EE', 'Early education'), ('PK', 'Pre-kindergarten'), ('KG', 'Kindergarten'), ('01', '1st grade'), ('02', '2nd grade'), ('03', '3rd grade'), ('04', '4th grade'), ('05', '5th grade'), ('06', '6th grade'), ('07', '7th grade'), ('08', '8th grade'), ('09', '9th grade'), ('10', '10th grade'), ('11', '11th grade'), ('12', '12th grade')], verbose_name='Highest grade offered', max_length=2),
        ),
        migrations.AlterField(
            model_name='campus',
            name='low_grade',
            field=models.CharField(choices=[('EE', 'Early education'), ('PK', 'Pre-kindergarten'), ('KG', 'Kindergarten'), ('01', '1st grade'), ('02', '2nd grade'), ('03', '3rd grade'), ('04', '4th grade'), ('05', '5th grade'), ('06', '6th grade'), ('07', '7th grade'), ('08', '8th grade'), ('09', '9th grade'), ('10', '10th grade'), ('11', '11th grade'), ('12', '12th grade')], verbose_name='Lowest grade offered', max_length=2),
        ),
        migrations.AlterField(
            model_name='campusstats',
            name='accountability_rating',
            field=models.CharField(blank=True, choices=[('M', 'Met standard'), ('A', 'Met alternative standard'), ('I', 'Improvement required'), ('X', 'Not rated'), ('Z', 'Not rated'), ('Q', 'Not rated due to data integrity issue')], verbose_name='Accountability rating', default='', max_length=1),
        ),
    ]
