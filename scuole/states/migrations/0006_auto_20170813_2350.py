# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-13 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0005_auto_20170811_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statecohorts',
            name='enrolled_out_of_state_percent',
            field=models.FloatField(null=True),
        ),
    ]