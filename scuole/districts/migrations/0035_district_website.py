# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0034_districtstats_college_ready_graduates_math_limited_english_proficient_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='website',
            field=models.URLField(null=True, verbose_name='District website', blank=True),
        ),
    ]
