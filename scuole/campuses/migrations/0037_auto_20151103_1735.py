# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0036_campus_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='website',
            field=models.URLField(blank=True, verbose_name='Campus website', default=''),
        ),
    ]
