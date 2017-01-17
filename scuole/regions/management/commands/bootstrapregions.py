# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Region
from scuole.states.models import State

from slugify import slugify


class Command(BaseCommand):
    help = 'Bootstraps Region models using TEA data.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='TX')

        regions_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'region', 'reference', 'reference.csv')

        with open(regions_file, 'rU') as f:
            reader = csv.DictReader(f)

            regions = []

            for row in reader:
                regions.append(self.create_region(row))

            Region.objects.bulk_create(regions)

    def create_region(self, region):
        name = string.capwords(region['REGNNAME'].split(': ')[1])
        self.stdout.write('Creating {}...'.format(name))

        return Region(
            name=name,
            region_id=region['REGION'],
            slug=slugify(int(region['REGION'])),
            state=self.texas,
        )
