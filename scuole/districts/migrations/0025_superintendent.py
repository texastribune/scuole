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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Name of personnel')),
                ('role', models.CharField(max_length=100, verbose_name='Role of personnel')),
                ('email', models.EmailField(max_length=254, verbose_name='Email of personnel')),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20, verbose_name='Phone number of personnel')),
                ('phone_number_extension', models.CharField(default='', max_length=4, blank=True, verbose_name='Phone number extension')),
                ('fax_number', localflavor.us.models.PhoneNumberField(max_length=20, verbose_name='Fax number of personnel')),
                ('district', models.OneToOneField(related_name='superintendent_of', to='districts.District')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
