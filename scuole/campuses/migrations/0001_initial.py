# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Campus name', max_length=200)),
                ('slug', models.SlugField()),
                ('tea_id', models.CharField(help_text='TEA campus identifier', max_length=10)),
                ('phone', models.CharField(help_text='Campus phone number', max_length=10)),
                ('street', models.CharField(help_text='Campus street', max_length=100)),
                ('city', models.CharField(help_text='Campus city', max_length=200)),
                ('state', models.CharField(help_text='Campus state', max_length=5)),
                ('zip_code', models.CharField(help_text='Campus ZIP Code', max_length=5)),
                ('zip_code4', models.CharField(help_text='Campus +4 ZIP Code', max_length=4)),
                ('status', models.CharField(help_text='Campus NCES status code', max_length=1)),
                ('locale', models.CharField(help_text='Campus NCES urban-centric locale code', max_length=2)),
                ('latitude', models.FloatField(help_text='Campus latitude')),
                ('longitude', models.FloatField(help_text='Campus longitude')),
                ('district', models.ForeignKey(related_name='campuses', to='districts.District')),
            ],
        ),
    ]
