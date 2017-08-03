# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-02 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0012_auto_20170801_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecohorts',
            name='economic_status',
            field=models.CharField(choices=[('Economically Disadvantaged', 'Economically Disadvantaged'), ('Not Economically Disadvantaged', 'Not Economically Disadvantaged')], max_length=2, null=True, verbose_name='Economic status'),
        ),
        migrations.AlterField(
            model_name='statecohorts',
            name='ethnicity',
            field=models.CharField(choices=[('White', 'White'), ('Hispanic', 'Hispanic'), ('African American', 'African American'), ('Others', 'Others')], max_length=16, null=True, verbose_name='Ethnicity'),
        ),
        migrations.AlterField(
            model_name='statecohorts',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=2, null=True, verbose_name='Gender'),
        ),
    ]
