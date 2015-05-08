# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_auto_20150508_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Geographic name for region', max_length=20)),
                ('region_id', models.CharField(help_text='Region identifier', max_length=2)),
                ('state', models.ForeignKey(related_name='regions', to='states.State')),
            ],
        ),
    ]
