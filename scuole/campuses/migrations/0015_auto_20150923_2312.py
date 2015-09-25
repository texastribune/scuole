# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0014_auto_20150922_2333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'campuses', 'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='campus',
            name='school_type',
            field=models.CharField(max_length=1, verbose_name='School type', choices=[('E', 'Elementary school'), ('M', 'Middle school or junior high school'), ('S', 'High school'), ('B', 'Elementary/secondary school')], default='E'),
            preserve_default=False,
        ),
    ]
