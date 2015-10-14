# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0027_auto_20151014_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='phone_number_extension',
            field=models.CharField(default='', max_length=4, verbose_name='Phone number extension', blank=True),
        ),
    ]
