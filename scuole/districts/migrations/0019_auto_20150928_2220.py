# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0018_auto_20150925_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='districtstats',
            old_name='avg_act_score_native_american',
            new_name='avg_act_score_american_indian',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='avg_sat_score_native_american',
            new_name='avg_sat_score_american_indian',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='college_ready_graduates_both_native_american_count',
            new_name='college_ready_graduates_both_american_indian_count',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='college_ready_graduates_both_native_american_percent',
            new_name='college_ready_graduates_both_american_indian_percent',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='college_ready_graduates_english_native_american_count',
            new_name='college_ready_graduates_english_american_indian_count',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='college_ready_graduates_english_native_american_percent',
            new_name='college_ready_graduates_english_american_indian_percent',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='college_ready_graduates_math_native_american_count',
            new_name='college_ready_graduates_math_american_indian_count',
        ),
        migrations.RenameField(
            model_name='districtstats',
            old_name='college_ready_graduates_math_native_american_percent',
            new_name='college_ready_graduates_math_american_indian_percent',
        ),
    ]
