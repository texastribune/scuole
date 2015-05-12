# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_auto_20150508_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='County name', max_length=100)),
                ('slug', models.SlugField()),
                ('fips', models.CharField(help_text='County fips code', max_length=3)),
                ('state', models.ForeignKey(related_name='counties', to='states.State')),
            ],
        ),
    ]
