# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionStats',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('all_students_count', models.IntegerField(verbose_name='Number of students')),
                ('african_american_count', models.IntegerField(verbose_name='Number of African American students')),
                ('asian_count', models.IntegerField(verbose_name='Number of Asian students')),
                ('hispanic_count', models.IntegerField(verbose_name='Number of Hispanic students')),
                ('pacific_islander_count', models.IntegerField(verbose_name='Number of Pacific Islander students')),
                ('two_or_more_races_count', models.IntegerField(verbose_name='Number of Two or More Races students')),
                ('white_count', models.IntegerField(verbose_name='Number of White students')),
                ('region', models.ForeignKey(related_name='stats', to='regions.Region')),
                ('year', models.ForeignKey(related_name='region_stats', to='stats.SchoolYear')),
            ],
            options={
                'verbose_name_plural': 'Region stats',
            },
        ),
        migrations.AlterUniqueTogether(
            name='regionstats',
            unique_together=set([('region', 'year')]),
        ),
    ]
