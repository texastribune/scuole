# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictStats',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('all_students_count', models.IntegerField(verbose_name='Number of students')),
                ('asian_count', models.IntegerField(verbose_name='Number of Asian students')),
                ('hispanic_count', models.IntegerField(verbose_name='Number of Hispanic students')),
                ('pacific_islander_count', models.IntegerField(verbose_name='Number of Pacific Islander students')),
                ('white_count', models.IntegerField(verbose_name='Number of White students')),
                ('district', models.ForeignKey(to='districts.District', related_name='stats')),
                ('year', models.ForeignKey(to='stats.SchoolYear', related_name='district_stats')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
