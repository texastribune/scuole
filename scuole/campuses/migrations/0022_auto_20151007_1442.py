# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0021_auto_20150929_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(verbose_name='Campus phone number', max_length=20),
        ),
    ]
