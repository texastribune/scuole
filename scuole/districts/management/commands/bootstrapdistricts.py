# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os
import string

from slugify import slugify

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, Point, MultiPolygon

from scuole.core.utils import remove_charter_c
from scuole.counties.models import County
from scuole.regions.models import Region

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Bootstraps District models using TEA, FAST and AskTED data.'

    def handle(self, *args, **options):
        askted_file_location = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        self.askted_data = self.load_askted_file(askted_file_location)

        fast_file_location = os.path.join(
            settings.DATA_FOLDER, 'fast', 'fast-district.csv')

        self.fast_data = self.load_fast_file(fast_file_location)

        district_json = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'shapes', 'districts.geojson')

        self.shape_data = self.load_geojson_file(district_json)

        superintendent_csv = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district', 'superintendents.csv')

        self.superintendent_data = self.load_superintendent_file(
            superintendent_csv)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'reference.csv')

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_district(row)

    def load_askted_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['District Number'].replace("'", "")
                payload[tea_id] = row

        return payload

    def load_fast_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['District Number']] = row

        return payload

    def load_geojson_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            data = json.load(f)

            for feature in data['features']:
                tea_id = feature['properties']['DISTRICT_C']
                payload[tea_id] = feature['geometry']

        return payload

    def load_superintendent_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['District Number'].replace("'", "")
                payload[tea_id] = row

        return payload

    def create_district(self, district):
        fast_match = self.fast_data[str(int(district['DISTRICT']))]
        shape_match = self.shape_data

        name = remove_charter_c(fast_match['District Name'])
        self.stdout.write('Creating {}...'.format(name))
        county = County.objects.get(name__iexact=district['CNTYNAME'])
        region = Region.objects.get(region_id=district['REGION'])
        if district['DISTRICT'] in shape_match:
            geometry = GEOSGeometry(
                json.dumps(shape_match[district['DISTRICT']]))

            # checks to see if the geometry is a multipolygon
            if geometry.geom_typeid == 3:
                geometry = MultiPolygon(geometry)
        else:
            self.stderr.write('No shape data for {}'.format(name))
            geometry = None

        if district['DISTRICT'] in self.askted_data:
            askted_match = self.askted_data[district['DISTRICT']]
            phone_number = askted_match['District Phone']
            if 'ext' in phone_number:
                phone_number, phone_number_extension = phone_number.split(
                    ' ext:')
                phone_number_extension = str(phone_number_extension)
            else:
                phone_number_extension = ''
            street = askted_match['District Street Address']
            city = askted_match['District City']
            state = askted_match['District State']
            zip_code = askted_match['District Zip']
        else:
            self.stderr.write('No askted data for {}'.format(name))
            askted_match = ''
            phone_number = ''
            phone_number_extension = ''
            street = ''
            city = ''
            state = ''
            zip_code = ''

        instance, _ = District.objects.update_or_create(
            tea_id=district['DISTRICT'],
            defaults={
                'name': name,
                'slug': slugify(name),
                'phone_number': phone_number,
                'phone_number_extension': phone_number_extension,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                'region': region,
                'county': county,
                'accountability_rating': district['D_RATING'],
                'shape': geometry,
            }
        )

        if district['DISTRICT'] in self.superintendent_data:
            superintendent = self.superintendent_data[
                district['DISTRICT']]
            self.load_superintendent(instance, superintendent)
        else:
            self.stderr.write('No superintendent data for {}'.format(name))

    def load_superintendent(self, district, superintendent):
        name = '{} {}'.format(
            superintendent['First Name'], superintendent['Last Name'])
        name = string.capwords(name)
        phone_number = superintendent['Phone']
        fax_number = superintendent['Fax']

        if 'ext' in phone_number:
            phone_number, phone_number_extension = phone_number.split(' ext:')
            phone_number_extension = str(phone_number_extension)
        else:
            phone_number_extension = ''

        if 'ext' in fax_number:
            fax_number, fax_number_extension = fax_number.split(' ext:')
            fax_number_extension = str(phone_number_extension)
        else:
            fax_number_extension = ''

        Superintendent.objects.update_or_create(
            name=name,
            district=district,
            defaults={
                'role': string.capwords(superintendent['Role']),
                'email': superintendent['Email Address'],
                'phone_number': phone_number,
                'phone_number_extension': phone_number_extension,
                'fax_number': fax_number,
                'fax_number_extension': fax_number_extension,
            }
        )
