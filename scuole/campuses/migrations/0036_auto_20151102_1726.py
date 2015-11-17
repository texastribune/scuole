# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0035_campusstats_college_ready_graduates_math_limited_english_proficient_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='campusstats',
            name='economically_disadvantaged_count',
            field=models.IntegerField(null=True, verbose_name='Number of economically disadvantaged students', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='economically_disadvantaged_percent',
            field=models.FloatField(null=True, verbose_name='Percent of economically disadvantaged students', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='limited_english_proficient_count',
            field=models.IntegerField(null=True, verbose_name='Number of limited English proficient students', blank=True),
        ),
        migrations.AddField(
            model_name='campusstats',
            name='limited_english_proficient_percent',
            field=models.FloatField(null=True, verbose_name='Percent of limited English proficient students', blank=True),
        ),
    ]
