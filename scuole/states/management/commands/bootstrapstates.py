# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon

from scuole.states.models import State, Commissioner


class Command(BaseCommand):
    help = 'Bootstraps state models.'

    def handle(self, *args, **options):

        state_json = os.path.join(
            settings.DATA_FOLDER,
            'state', 'shape', 'tx.geojson')

        self.shape_data = self.load_geojson_file(state_json)

        commissioner_csv = os.path.join(
            settings.DATA_FOLDER,
            'state', 'commissioner.csv')

        self.commissioner_data = self.load_commissioner_file(
            commissioner_csv)

        self.create_state()

    def load_geojson_file(self, file):
        payload = {}

        with open(file, 'rU') as f:
            data = json.load(f)

            for feature in data['features']:
                payload = feature['geometry']

        return payload

    def load_commissioner_file(self, file):
        with open(file, 'rU') as f:
            reader = csv.DictReader(f)
            return next(reader)

    def create_state(self):
        self.stdout.write('Creating Texas...')

        geometry = GEOSGeometry(
            json.dumps(self.shape_data))

        # checks to see if the geometry is a multipolygon
        if geometry.geom_typeid == 3:
            geometry = MultiPolygon(geometry)

        state, _ = State.objects.update_or_create(
            slug='tx',
            defaults={
                'name': 'TX',
                'shape': geometry
            }
        )

        commissioner = self.commissioner_data
        self.load_commissioner(state, commissioner)

    def load_commissioner(self, state, commissioner):
        name = commissioner['Full Name']
        Commissioner.objects.update_or_create(
            state=state,
            defaults={
                'name': name,
                'role': commissioner['Role'],
                'phone_number': commissioner['Phone'],
            }
        )
