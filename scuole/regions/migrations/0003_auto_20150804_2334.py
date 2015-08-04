# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_auto_20150730_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionstats',
            name='african_american_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of African American students'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='all_students_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of students'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='asian_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of Asian students'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='hispanic_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of Hispanic students'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='pacific_islander_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of Pacific Islander students'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='two_or_more_races_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of Two or More Races students'),
        ),
        migrations.AddField(
            model_name='regionstats',
            name='white_percent',
            field=models.FloatField(null=True, blank=True, verbose_name='Percent of White students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='african_american_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of African American students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='all_students_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='asian_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of Asian students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='hispanic_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of Hispanic students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='pacific_islander_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of Pacific Islander students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='two_or_more_races_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of Two or More Races students'),
        ),
        migrations.AlterField(
            model_name='regionstats',
            name='white_count',
            field=models.IntegerField(null=True, blank=True, verbose_name='Number of White students'),
        ),
    ]
