# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from scuole.counties.models import County
from scuole.districts.models import District

from ...models import Campus

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

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', '2013-14', 'campus', 'campus-reference.csv')

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            campuses = []

            for row in reader:
                campuses.append(self.create_campus(row))

            Campus.objects.bulk_create(campuses)

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

    def create_campus(self, campus):
        ccd_match = self.ccd_data[campus['CAMPUS']]
        fast_match = self.fast_data[str(int(campus['CAMPUS']))]
        self.stdout.write('Creating {}...'.format(fast_match['Campus Name']))
        low_grade, high_grade = campus['GRDSPAN'].split(' - ')
        district = District.objects.get(tea_id=campus['DISTRICT'])
        county = County.objects.get(fips=ccd_match['CONUM'][-3:])

        return Campus(
            name=fast_match['Campus Name'],
            slug=slugify(fast_match['Campus Name']),
            tea_id=campus['CAMPUS'],
            phone=ccd_match['PHONE'],
            street=ccd_match['LSTREE'],
            city=ccd_match['LCITY'],
            state=ccd_match['LSTATE'],
            zip_code=ccd_match['LZIP'],
            zip_code4=ccd_match['LZIP4'],
            locale=LOCALE_MAP[ccd_match['ULOCAL']],
            latitude=ccd_match['LATCOD'],
            longitude=ccd_match['LONCOD'],
            low_grade=low_grade,
            high_grade=high_grade,
            district=district,
            county=county,
        )
