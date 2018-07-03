# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os
import string

from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand

from slugify import slugify

from scuole.states.models import State

from ...models import Region


class Command(BaseCommand):
    help = 'Bootstraps Region models using TEA data.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='TX')

        regions_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'region', 'reference', 'reference.csv')

        region_json = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'region', 'shapes', 'regions.geojson')

        self.shape_data = self.load_geojson_file(region_json)

        with open(regions_file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_region(row)

    def load_geojson_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            data = json.load(f)

            for feature in data['features']:
                tea_id = feature['properties']['REGION']
                payload[tea_id] = feature['geometry']

        return payload

    def create_region(self, region):
        name = string.capwords(region['REGNNAME'].split(': ')[1])
        self.stdout.write('Creating {}...'.format(name))

        geometry = GEOSGeometry(
            json.dumps(self.shape_data[region['REGION']]))

        # checks to see if the geometry is a multipolygon
        if geometry.geom_typeid == 3:
            geometry = MultiPolygon(geometry)

        region, _ = Region.objects.update_or_create(
            region_id=region['REGION'],
            defaults={
                'name': name,
                'slug': slugify(region['REGION']),
                'shape': geometry,
                'state': self.texas,
            }
        )
