# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os
import string

from slugify import slugify

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry

from scuole.core.utils import remove_charter_c
from scuole.counties.models import County
from scuole.districts.models import District

from ...models import Campus, Principal

LOCALE_MAP = {
    '11': 'LARGE_CITY',
    '12': 'MID_SIZE_CITY',
    '13': 'SMALL_CITY',
    '21': 'LARGE_SUBURB',
    '22': 'MID_SIZE_SUBURB',
    '23': 'SMALL_SUBURB',
    '31': 'FRINGE_TOWN',
    '32': 'DISTANT_TOWN',
    '33': 'REMOTE_TOWN',
    '41': 'FRINGE_RURAL',
    '42': 'DISTANT_RURAL',
    '43': 'REMOTE_RURAL',
}


class Command(BaseCommand):
    help = 'Bootstraps Campus models using TEA, FAST and AskTED data.'

    def handle(self, *args, **options):
        askted_file_location = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        self.askted_data = self.load_askted_file(askted_file_location)

        fast_file_location = os.path.join(
            settings.DATA_FOLDER, 'fast', 'fast-campus.csv')

        self.fast_data = self.load_fast_file(fast_file_location)

        campus_json = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'campus', 'shapes', 'campuses.geojson')

        self.shape_data = self.load_geojson_file(campus_json)

        principal_csv = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'campus', 'principals.csv')

        self.principal_data = self.load_principal_file(
            principal_csv)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'campus', 'reference.csv')

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_campus(row)

    def load_askted_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['School Number'].replace("'", "")
                payload[tea_id] = row

        return payload

    def load_fast_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['Campus Number']] = row

        return payload

    def load_geojson_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            data = json.load(f)

            for feature in data['features']:
                tea_id = feature['properties']['CAMPUS']
                payload[tea_id] = feature['geometry']

        return payload

    def load_principal_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['Organization Number'].replace("'", "")

                if tea_id not in payload:
                    payload[tea_id] = []

                payload[tea_id].append(row)

        return payload

    def create_campus(self, campus):
        fast_match = self.fast_data[str(int(campus['CAMPUS']))]
        name = remove_charter_c(fast_match['Campus Name'])

        self.stdout.write('Creating {}...'.format(name))

        low_grade, high_grade = campus['GRDSPAN'].split(' - ')
        district = District.objects.get(tea_id=campus['DISTRICT'])
        county = County.objects.get(name__iexact=campus['CNTYNAME'])

        if campus['CAMPUS'] in self.shape_data:
            geometry = GEOSGeometry(
                json.dumps(self.shape_data[campus['CAMPUS']])
            )
        else:
            self.stderr.write('No shape data for {}'.format(name))
            geometry = None

        if campus['CAMPUS'] in self.askted_data:
            askted_match = self.askted_data[campus['CAMPUS']]
            phone_number = askted_match['School Phone']
            if 'ext' in phone_number:
                phone_number, phone_number_extension = phone_number.split(
                    ' ext:')
                phone_number_extension = str(phone_number_extension)
            else:
                phone_number_extension = ''
            street = askted_match['School Street Address']
            city = askted_match['School City']
            state = askted_match['School State']
            zip_code = askted_match['School Zip']
        else:
            self.stderr.write('No askted data for {}'.format(name))
            phone_number = ''
            phone_number_extension = ''
            street = ''
            city = ''
            state = ''
            zip_code = ''

        instance, _ = Campus.objects.update_or_create(
            tea_id=campus['CAMPUS'],
            defaults={
                'name': name,
                'slug': slugify(name),
                'phone_number': phone_number,
                'phone_number_extension': phone_number_extension,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                'coordinates': geometry,
                'low_grade': low_grade,
                'high_grade': high_grade,
                'school_type': campus['GRDTYPE'],
                'district': district,
                'county': county,
            }
        )

        if campus['CAMPUS'] in self.principal_data:
            instance_principals = self.principal_data[campus['CAMPUS']]

            self.load_principals(instance, instance_principals)
        else:
            self.stderr.write('No principal data for {}'.format(name))

    def load_principals(self, campus, principals):
        for principal in principals:
            name = '{} {}'.format(
                principal['First Name'], principal['Last Name'])
            name = string.capwords(name)
            phone_number = principal['Phone']
            fax_number = principal['Fax']

            if 'ext' in phone_number:
                phone_number, phone_number_extension = phone_number.split(
                    ' ext:')
                phone_number_extension = str(phone_number_extension)
            else:
                phone_number_extension = ''

            if 'ext' in fax_number:
                fax_number, fax_number_extension = fax_number.split(' ext:')
                fax_number_extension = str(phone_number_extension)
            else:
                fax_number_extension = ''

            Principal.objects.update_or_create(
                name=name,
                campus=campus,
                defaults={
                    'role': string.capwords(principal['Role']),
                    'email': principal['Email Address'],
                    'phone_number': phone_number,
                    'phone_number_extension': phone_number_extension,
                    'fax_number': fax_number,
                    'fax_number_extension': fax_number_extension,
                }
            )
