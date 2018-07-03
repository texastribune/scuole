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

from ...models import County


class Command(BaseCommand):
    help = 'Bootstraps County models using DSHS county list.'

    def handle(self, *args, **options):
        self.texas = State.objects.get(name='TX')

        counties_file = os.path.join(
            settings.DATA_FOLDER, 'counties', 'counties.csv')

        county_json = os.path.join(
            settings.DATA_FOLDER, 'counties', 'shapes', 'counties.geojson')

        self.shape_data = self.load_geojson_file(county_json)

        with open(counties_file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_county(row)

    def load_geojson_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            data = json.load(f)

            for feature in data['features']:
                tea_id = str(feature['properties']['FIPS']).zfill(3)
                payload[tea_id] = feature['geometry']

        return payload

    def create_county(self, county):
        fips = county['FIPS #'].zfill(3)
        self.stdout.write(
            'Creating {} County...'.format(county['County Name']))

        geometry = GEOSGeometry(json.dumps(self.shape_data[fips]))

        # checks to see if the geometry is a multipolygon
        if geometry.geom_typeid == 3:
            geometry = MultiPolygon(geometry)

        county, _ = County.objects.update_or_create(
            fips=fips,
            defaults={
                'name': county['County Name'],
                'slug': slugify(county['County Name']),
                'shape': geometry,
                'state': self.texas,
            }
        )
