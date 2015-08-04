# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0002_districtstats'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='districtstats',
            unique_together=set([('district', 'year')]),
        ),
    ]
