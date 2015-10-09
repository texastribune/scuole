# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0025_superintendent'),
    ]

    operations = [
        migrations.AddField(
            model_name='superintendent',
            name='fax_number_extension',
            field=models.CharField(max_length=4, blank=True, verbose_name='Fax number extension', default=''),
        ),
    ]
