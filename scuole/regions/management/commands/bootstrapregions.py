# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string

from django.conf import settings
from django.core.management.base import BaseCommand

from ...forms import RegionAddForm
from scuole.states.models import State


class Command(BaseCommand):
    help = 'Bootstraps Region models using TEA data.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='TX')

        regions_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr',
            '2013-2014',
            'region',
            'reference.csv')

        with open(regions_file, 'r') as f:
            reader = csv.DictReader(f)

            count = 0
            errors = []

            for row in reader:
                data = self.reformat_data(row)
                form = RegionAddForm(data)

                if form.is_valid():
                    region_instance = form.save(commit=False)
                    region_instance.state = self.texas
                    region_instance.save()
                    count += 1
                else:
                    errors.append(form.errors)

            self.stdout.write('Regions created: {}'.format(count))
            if errors:
                self.stderr.write('Errors: {}'.format(len(errors)))

    def reformat_data(self, row):
        return {
            'name': string.capwords(row['REGNNAME'].split(': ')[1]),
            'region_id': row['REGION'],
        }
