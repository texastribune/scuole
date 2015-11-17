# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


# def create_texas(apps, schema_editor):
#     State = apps.get_model('states', 'State')

#     State.objects.create(
#         name='TX',
#         slug='tx',
#     )


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
    ]

    operations = [
        # migrations.RunPython(create_texas),
    ]
