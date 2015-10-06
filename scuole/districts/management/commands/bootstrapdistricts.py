# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, Point, MultiPolygon

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

        district_json = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'shapes', 'SchoolDistricts.geojson')

        self.shape_data = self.load_geojson_file(district_json)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'reference.csv')

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

    def load_geojson_file(self, file):
        feature = {}

        with open(file, 'r') as f:
            reader = json.load(f)

            for feature in reader['features']:
                feature['geometry']['type']

        return feature


    def create_district(self, district):
        ccd_match = self.ccd_data[district['DISTRICT']]
        fast_match = self.fast_data[str(int(district['DISTRICT']))]
        shape_match = self.shape_data
        self.stdout.write('Creating {}...'.format(fast_match['District Name']))
        name = remove_charter_c(fast_match['District Name'])
        county = County.objects.get(fips=ccd_match['CONUM'][-3:])
        region = Region.objects.get(region_id=district['REGION'])
        pnt = Point(float(ccd_match['LONCOD']), float(ccd_match['LATCOD']))
        geometry = GEOSGeometry(json.dumps(shape_match['geometry']))

        # checks to see if the geometry is a multipolygon
        if geometry.geom_typeid == 3:
            geometry = MultiPolygon(geometry)

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
            latlong=pnt,
            region=region,
            county=county,
            mpoly=geometry,
        )
