# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0028_auto_20151014_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(max_length=20, null=True, verbose_name='District phone number'),
        ),
        migrations.AddField(
            model_name='district',
            name='phone_number_extension',
            field=models.CharField(default='', max_length=4, verbose_name='Phone number extension', blank=True),
        ),
    ]
