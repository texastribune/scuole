# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os
import string

from slugify import slugify

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from django.contrib.gis.geos import GEOSGeometry

from scuole.core.utils import remove_charter_c
from scuole.counties.models import County
from scuole.districts.models import District

from ...models import Campus, Principal

from scuole.core.replacements import ISD_REPLACEMENT
from scuole.core.utils import massage_name

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

    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

        # path to askTed file
        askted_file = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        self.askted_data = self.load_askted_file(askted_file)

        # path to FAST file where original cleaned up names are stored
        fast_file = os.path.join(
            settings.DATA_FOLDER, 'fast', 'fast-campus.csv')

        self.fast_data = self.load_fast_file(fast_file)

        # path to TAPR file where campus shapefiles are stored
        campus_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'campus', 'shapes', 'campuses.geojson')

        self.shape_data = self.load_geojson_file(campus_file)

        # path to askTed file where principal information is stored
        principal_file = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'campus', 'principals.csv')

        self.principal_data = self.load_principal_file(
            principal_file)

        # path to file where new, cleaned up campus names and IDs are stored
        new_campuses = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'campus', 'updates', options['year'],
            'new_campuses.csv')

        self.newCampus_data = self.load_newCampus_file(new_campuses)

        # path to file where new, cleaned up names and IDs of campuses whose
        # names have changed since the last update
        changed_campuses = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'campus', 'updates', options['year'],
            'changed_campuses.csv')

        self.changedCampus_data = self.load_changedCampus_file(changed_campuses)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'campus', 'reference', 'reference.csv')

        with open(tea_file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_campus(row)

        self.make_slugs_unique()

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

    def load_newCampus_file(self, file):
        payload = {}

        with open(file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['Campus Number']
                payload[tea_id] = row

        return payload

    def load_changedCampus_file(self, file):
        payload = {}

        with open(file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['Campus Number']
                payload[tea_id] = row

        return payload

    def create_campus(self, campus):
        campus_id = str(int(campus['CAMPUS']))

        if campus_id in self.fast_data:
            fast_match = self.fast_data[campus_id]
        elif campus_id in self.newCampus_data:
            fast_match = self.newCampus_data[campus_id]
        elif campus_id in self.changedCampus_data:
            fast_match = self.changedCampus_data[campus_id]
        else:
            fast_match = {
                'Campus Name': massage_name(
                    campus['CAMPNAME'], ISD_REPLACEMENT)
            }

        name = remove_charter_c(fast_match['Campus Name'])
        self.stdout.write('Creating {}...'.format(name))

        low_grade, high_grade = campus['GRDSPAN'].split(' - ')
        district = District.objects.get(tea_id=campus['DISTRICT'])
        county = County.objects.get(name__iexact=campus['CNTYNAME'])

        if campus['CFLCHART'] == 'N':
            charter = False
        else:
            charter = True

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
            website = askted_match['School Web Page Address']
        else:
            self.stderr.write('No askted data for {}'.format(name))
            phone_number = ''
            phone_number_extension = ''
            street = ''
            city = ''
            state = ''
            zip_code = ''
            website = ''

        instance, _ = Campus.objects.update_or_create(
            tea_id=campus['CAMPUS'],
            defaults={
                'name': name,
                'slug': slugify(name),
                'phone_number': phone_number,
                'phone_number_extension': phone_number_extension,
                'website': website,
                'charter': charter,
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

    def make_slugs_unique(self):
        for district in District.objects.all():

            models = district.campuses.values('slug').annotate(
                Count('slug')).order_by().filter(slug__count__gt=1)
            slugs = [i['slug'] for i in models]

            campuses = district.campuses.filter(slug__in=slugs)

            for campus in campuses:
                campus.slug = '{0}-{1}-{2}'.format(
                    campus.slug, campus.low_grade, campus.high_grade)
                campus.save()

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
