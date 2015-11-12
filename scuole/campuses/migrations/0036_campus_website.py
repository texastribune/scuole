# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0035_campusstats_college_ready_graduates_math_limited_english_proficient_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='website',
            field=models.URLField(null=True, verbose_name='Campus website', blank=True),
        ),
    ]
