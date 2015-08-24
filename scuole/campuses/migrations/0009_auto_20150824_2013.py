# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0008_auto_20150824_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='zip_code4',
        ),
        migrations.AlterField(
            model_name='campus',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(verbose_name='Campus ZIP Code', max_length=10),
        ),
    ]
