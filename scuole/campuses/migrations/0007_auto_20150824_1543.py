# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0006_remove_campusstats_all_students_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='city',
            field=models.CharField(max_length=200, verbose_name='Campus city'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='high_grade',
            field=models.CharField(max_length=2, verbose_name='Highest grade offered', choices=[('EE', 'Early education'), ('PK', 'Pre-kindergarten'), ('KG', 'Kindergarten'), ('01', '1st Grade'), ('02', '2nd Grade'), ('03', '3rd Grade'), ('04', '4th Grade'), ('05', '5th Grade'), ('06', '6th Grade'), ('07', '7th Grade'), ('08', '8th Grade'), ('09', '9th Grade'), ('10', '10th Grade'), ('11', '11th Grade'), ('12', '12th Grade')]),
        ),
        migrations.AlterField(
            model_name='campus',
            name='latitude',
            field=models.FloatField(verbose_name='Campus latitude'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='locale',
            field=models.CharField(max_length=15, verbose_name='Campus NCES urban-centric locale identifier'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='longitude',
            field=models.FloatField(verbose_name='Campus longitude'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='low_grade',
            field=models.CharField(max_length=2, verbose_name='Lowest grade offered', choices=[('EE', 'Early education'), ('PK', 'Pre-kindergarten'), ('KG', 'Kindergarten'), ('01', '1st Grade'), ('02', '2nd Grade'), ('03', '3rd Grade'), ('04', '4th Grade'), ('05', '5th Grade'), ('06', '6th Grade'), ('07', '7th Grade'), ('08', '8th Grade'), ('09', '9th Grade'), ('10', '10th Grade'), ('11', '11th Grade'), ('12', '12th Grade')]),
        ),
        migrations.AlterField(
            model_name='campus',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Campus name'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Campus phone number'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='state',
            field=models.CharField(max_length=5, verbose_name='Campus state'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Campus street'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='tea_id',
            field=models.CharField(max_length=10, verbose_name='TEA campus identifier'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='zip_code',
            field=models.CharField(max_length=5, verbose_name='Campus ZIP Code'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='zip_code4',
            field=models.CharField(max_length=4, verbose_name='Campus +4 ZIP Code'),
        ),
    ]
