# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='District name', max_length=200)),
                ('slug', models.SlugField()),
                ('tea_id', models.CharField(help_text='TEA district identifier', max_length=6)),
                ('street', models.CharField(help_text='District street', max_length=200)),
                ('city', models.CharField(help_text='District office city', max_length=100)),
                ('state', models.CharField(help_text='District office abbreviated state location', max_length=2)),
                ('zip_code', models.CharField(help_text='District office ZIP Code', max_length=5)),
                ('zip_code4', models.CharField(help_text='District office +4 ZIP Code', max_length=4)),
                ('latitude', models.FloatField(help_text='District office latitude')),
                ('longitude', models.FloatField(help_text='District office longitude')),
            ],
        ),
    ]
