# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0024_auto_20151008_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Superintendent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Name of personnel', max_length=254)),
                ('role', models.CharField(verbose_name='Role of personnel', max_length=100)),
                ('email', models.EmailField(verbose_name='Email of personnel', max_length=254)),
                ('phone_number', localflavor.us.models.PhoneNumberField(verbose_name='Phone number of personnel', max_length=20)),
                ('phone_number_extension', models.IntegerField(blank=True, verbose_name='Phone number extension', null=True)),
                ('fax_number', localflavor.us.models.PhoneNumberField(verbose_name='Fax number of personnel', max_length=20)),
                ('district', models.ForeignKey(to='districts.District', related_name='superintendent_of')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
