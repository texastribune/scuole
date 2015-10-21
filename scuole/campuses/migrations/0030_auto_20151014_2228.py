# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0029_auto_20151014_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(max_length=20, null=True, verbose_name='Campus phone number'),
        ),
    ]
