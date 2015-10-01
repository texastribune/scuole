# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping

from scuole.core.utils import remove_charter_c
from scuole.counties.models import County
from scuole.regions.models import Region

from ...models import District

from slugify import slugify


class Command(BaseCommand):
    help = 'Bootstraps District models using TEA, FAST and CCD data.'

    def handle(self, *args, **options):
        ccd_file_location = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-districts-ccd.csv')

        self.ccd_data = self.load_ccd_file(ccd_file_location)

        fast_file_location = os.path.join(
            settings.DATA_FOLDER, 'fast', 'fast-district.csv')

        self.fast_data = self.load_fast_file(fast_file_location)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'reference.csv')

        district_mapping = {
            'mpoly' : 'MULTIPOLYGON',
        }

        district_shp = os.path.abspath(os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'shapes', 'SchoolDistricts.shp'))

        def run(verbose=True):
            lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                              transform=False, encoding='iso-8859-1')

            lm.save(strict=True, verbose=verbose)

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            districts = []

            for row in reader:
                districts.append(self.create_district(row))

            District.objects.bulk_create(districts)

    def load_ccd_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['STID']] = row

        return payload

    def load_fast_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['District Number']] = row

        return payload

    def create_district(self, district):
        ccd_match = self.ccd_data[district['DISTRICT']]
        fast_match = self.fast_data[str(int(district['DISTRICT']))]
        self.stdout.write('Creating {}...'.format(fast_match['District Name']))
        name = remove_charter_c(fast_match['District Name'])
        county = County.objects.get(fips=ccd_match['CONUM'][-3:])

        return District(
            name=name,
            slug=slugify(name),
            tea_id=district['DISTRICT'],
            street=ccd_match['LSTREE'],
            city=ccd_match['LCITY'],
            state=ccd_match['LSTATE'],
            zip_code='{LZIP}-{LZIP4}'.format(
                LZIP=ccd_match['LZIP'],
                LZIP4=ccd_match['LZIP4']),
            latitude=ccd_match['LATCOD'],
            longitude=ccd_match['LONCOD'],
            region=Region.objects.get(region_id=district['REGION']),
            county=county,
        )
