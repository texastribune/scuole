# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0035_district_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='website',
            field=models.URLField(blank=True, verbose_name='District website', default=''),
        ),
    ]
