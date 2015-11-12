# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0034_auto_20151028_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='campusstats',
            name='college_ready_graduates_math_limited_english_proficient_count',
            field=models.IntegerField(null=True, verbose_name='Number of college ready limited english proficient graduates in math', db_column='college_ready_graduates_math_lep_count', blank=True),
        ),
    ]
