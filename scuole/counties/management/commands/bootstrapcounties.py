# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...forms import CountyAddForm
from scuole.states.models import State


class Command(BaseCommand):
    help = 'Bootstraps County models using the DSHS county list.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='TX')

        counties_file = os.path.join(
            settings.DATA_FOLDER, 'counties', 'counties.csv')

        with open(counties_file, 'rU') as f:
            reader = csv.DictReader(f)

            count = 0
            errors = []

            for row in reader:
                data = self.reformat_data(row)
                form = CountyAddForm(data)

                if form.is_valid():
                    county_instance = form.save(commit=False)
                    county_instance.state = self.texas
                    county_instance.save()
                    count += 1
                else:
                    errors.append(form.errors)

            self.stdout.write('Counties created: {}'.format(count))
            if errors:
                self.stderr.write('Errors: {}'.format(len(errors)))

    def reformat_data(self, row):
        return {
            'name': row['County Name'],
            'fips': row['FIPS #'].zfill(3),
        }
