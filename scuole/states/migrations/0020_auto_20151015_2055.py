# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0019_auto_20151008_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_fifth',
            field=models.FloatField(null=True, verbose_name='Average fifth grade class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_first',
            field=models.FloatField(null=True, verbose_name='Average first grade class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_fourth',
            field=models.FloatField(null=True, verbose_name='Average fourth grade class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_kindergarten',
            field=models.FloatField(null=True, verbose_name='Average kindergarten grade class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_mixed_elementary',
            field=models.FloatField(null=True, verbose_name='Average mixed elementary class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_second',
            field=models.FloatField(null=True, verbose_name='Average second grade class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_secondary_english',
            field=models.FloatField(null=True, verbose_name='Average secondary English class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_secondary_foreign_language',
            field=models.FloatField(null=True, verbose_name='Average secondary foreign language class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_secondary_math',
            field=models.FloatField(null=True, verbose_name='Average secondary math class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_secondary_science',
            field=models.FloatField(null=True, verbose_name='Average secondary science class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_secondary_social_studies',
            field=models.FloatField(null=True, verbose_name='Average secondary social studies class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_sixth',
            field=models.FloatField(null=True, verbose_name='Average sixth grade class size', blank=True),
        ),
        migrations.AddField(
            model_name='statestats',
            name='class_size_avg_third',
            field=models.FloatField(null=True, verbose_name='Average third grade class size', blank=True),
        ),
        migrations.AlterField(
            model_name='statestats',
            name='dropout_at_risk_count',
            field=models.IntegerField(null=True, verbose_name='Number of 9-12 white students who dropped out', blank=True),
        ),
    ]
