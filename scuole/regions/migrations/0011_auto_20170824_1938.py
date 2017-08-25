# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-24 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0010_auto_20170818_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regioncohorts',
            name='economic_status',
            field=models.CharField(blank=True, choices=[('Economically Disadvantaged', 'economically disadvantaged'), ('Not Economically Disadvantaged', 'not economically disadvantaged')], max_length=30, verbose_name='Economic status'),
        ),
        migrations.AlterField(
            model_name='regioncohorts',
            name='ethnicity',
            field=models.CharField(blank=True, choices=[('White', 'white'), ('Hispanic', 'hispanic'), ('African American', 'black'), ('Others', 'other'), ('All Ethnicities', 'unknown')], max_length=30, verbose_name='Ethnicity'),
        ),
        migrations.AlterField(
            model_name='regioncohorts',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'female'), ('Male', 'male')], max_length=30, verbose_name='Gender'),
        ),
    ]