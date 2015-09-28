# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0015_auto_20150928_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statestats',
            old_name='college_ready_graduates_english_two_or_more_count',
            new_name='college_ready_graduates_english_two_or_more_races_count',
        ),
        migrations.RenameField(
            model_name='statestats',
            old_name='college_ready_graduates_english_two_or_more_percent',
            new_name='college_ready_graduates_english_two_or_more_races_percent',
        ),
    ]
