# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-02 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0015_auto_20170802_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regioncohorts',
            name='economic_status',
            field=models.CharField(choices=[('Economically Disadvantaged', 'Economically Disadvantaged'), ('Not Economically Disadvantaged', 'Not Economically Disadvantaged')], max_length=30, null=True, verbose_name='Economic status'),
        ),
        migrations.AlterField(
            model_name='regioncohorts',
            name='ethnicity',
            field=models.CharField(choices=[('White', 'White'), ('Hispanic', 'Hispanic'), ('African American', 'African American'), ('Others', 'Others')], max_length=30, null=True, verbose_name='Ethnicity'),
        ),
        migrations.AlterField(
            model_name='regioncohorts',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=30, null=True, verbose_name='Gender'),
        ),
    ]
