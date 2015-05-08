# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from ...models import County
from scuole.states.models import State


class Command(BaseCommand):
    help = 'Bootstraps County models using DSHS county list.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='Texas')

        counties_file = os.path.join(
            settings.DATA_FOLDER, 'counties', 'counties.csv')

        with open(counties_file, 'rU') as f:
            reader = csv.DictReader(f)

            counties = []

            for row in reader:
                counties.append(self.create_county(row))

            County.objects.bulk_create(counties)

    def create_county(self, county):
        return County(
            name=county['County Name'],
            slug=slugify(county['County Name']),
            fips=county['FIPS #'],
            state=self.texas,
        )
