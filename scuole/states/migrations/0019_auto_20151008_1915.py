# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0018_auto_20150929_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statestats',
            name='american_indian_count',
            field=models.IntegerField(null=True, verbose_name='Number of American Indian students', blank=True),
        ),
    ]
