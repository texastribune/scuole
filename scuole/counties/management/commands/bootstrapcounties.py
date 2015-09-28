# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import County
from scuole.states.models import State

from slugify import slugify


class Command(BaseCommand):
    help = 'Bootstraps County models using DSHS county list.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='TX')

        counties_file = os.path.join(
            settings.DATA_FOLDER, 'counties', 'counties.csv')

        with open(counties_file, 'rU') as f:
            reader = csv.DictReader(f)

            counties = []

            for row in reader:
                counties.append(self.create_county(row))

            County.objects.bulk_create(counties)

    def create_county(self, county):
        self.stdout.write(
            'Creating {} County...'.format(county['County Name']))

        return County(
            name=county['County Name'],
            slug=slugify(county['County Name']),
            fips=county['FIPS #'].zfill(3),
            state=self.texas,
        )
