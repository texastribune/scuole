# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
        ('campuses', '0003_auto_20150729_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusStats',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('all_students_count', models.IntegerField(verbose_name='Number of students')),
                ('african_american_count', models.IntegerField(verbose_name='Number of African American students')),
                ('asian_count', models.IntegerField(verbose_name='Number of Asian students')),
                ('hispanic_count', models.IntegerField(verbose_name='Number of Hispanic students')),
                ('pacific_islander_count', models.IntegerField(verbose_name='Number of Pacific Islander students')),
                ('two_or_more_races_count', models.IntegerField(verbose_name='Number of Two or More Races students')),
                ('white_count', models.IntegerField(verbose_name='Number of White students')),
                ('campus', models.ForeignKey(related_name='stats', to='campuses.Campus')),
                ('year', models.ForeignKey(related_name='campus_stats', to='stats.SchoolYear')),
            ],
            options={
                'verbose_name_plural': 'Campus stats',
            },
        ),
        migrations.AlterUniqueTogether(
            name='campusstats',
            unique_together=set([('campus', 'year')]),
        ),
    ]
