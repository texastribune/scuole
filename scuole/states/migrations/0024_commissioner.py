# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0023_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commissioner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name='Name of personnel')),
                ('role', models.CharField(max_length=100, verbose_name='Role of personnel')),
                ('email', models.EmailField(max_length=254, verbose_name='Email of personnel')),
                ('phone_number', localflavor.us.models.PhoneNumberField(max_length=20, verbose_name='Phone number of personnel')),
                ('phone_number_extension', models.CharField(default='', max_length=4, verbose_name='Phone number extension', blank=True)),
                ('fax_number', localflavor.us.models.PhoneNumberField(max_length=20, verbose_name='Fax number of personnel')),
                ('fax_number_extension', models.CharField(default='', max_length=4, verbose_name='Fax number extension', blank=True)),
                ('state', models.OneToOneField(related_name='commissioner_of', to='states.State')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
