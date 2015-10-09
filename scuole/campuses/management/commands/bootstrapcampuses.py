# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string

from slugify import slugify

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

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
    help = 'Bootstraps Campus models using TEA, FAST and CCD data.'

    def handle(self, *args, **options):
        ccd_file_location = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-campuses-ccd.csv')

        self.ccd_data = self.load_ccd_file(ccd_file_location)

        fast_file_location = os.path.join(
            settings.DATA_FOLDER, 'fast', 'fast-campus.csv')

        self.fast_data = self.load_fast_file(fast_file_location)

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

    def load_ccd_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['SEASCH']] = row

        return payload

    def load_fast_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['Campus Number']] = row

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
        ccd_match = self.ccd_data[campus['CAMPUS']]
        fast_match = self.fast_data[str(int(campus['CAMPUS']))]
        name = remove_charter_c(fast_match['Campus Name'])
        self.stdout.write('Creating {}...'.format(name))
        low_grade, high_grade = campus['GRDSPAN'].split(' - ')
        district = District.objects.get(tea_id=campus['DISTRICT'])
        county = County.objects.get(fips=ccd_match['CONUM'][-3:])
        coordinates = Point(
            float(ccd_match['LONCOD']), float(ccd_match['LATCOD']))

        instance, _ = Campus.objects.update_or_create(
            tea_id=campus['CAMPUS'],
            defaults={
                'name': name,
                'slug': slugify(name),
                'phone': ccd_match['PHONE'],
                'street': ccd_match['LSTREE'],
                'city': ccd_match['LCITY'],
                'state': ccd_match['LSTATE'],
                'zip_code': '{LZIP}-{LZIP4}'.format(
                    LZIP=ccd_match['LZIP'],
                    LZIP4=ccd_match['LZIP4']),
                'locale': LOCALE_MAP[ccd_match['ULOCAL']],
                'coordinates': coordinates,
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
