# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0024_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='fax_number_extension',
            field=models.CharField(max_length=4, blank=True, verbose_name='Fax number extension', default=''),
        ),
    ]
