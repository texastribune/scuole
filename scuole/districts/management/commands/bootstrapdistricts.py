# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from scuole.counties.models import County
from scuole.regions.models import Region

from ...forms import DistrictAddForm


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
            'tapr', '2013-2014', 'district', 'reference.csv')

        self.count = 0
        self.errors = []

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_district(row)

        self.stdout.write('Districts created: {}'.format(self.count))
        if self.errors:
            self.stderr.write('Errors: {}'.format(len(self.errors)))

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

    def reformat_data(self, district):
        ccd_match = self.ccd_data[district['DISTRICT']]
        fast_match = self.fast_data[str(int(district['DISTRICT']))]

        if ccd_match['LZIP4']:
            zip_code = '{LZIP}-{LZIP4}'.format(
                LZIP=ccd_match['LZIP'],
                LZIP4=ccd_match['LZIP4'])
        else:
            zip_code = ccd_match['LZIP']

        return {
            'county': County.objects.get(fips=ccd_match['CONUM'][-3:]),
            'region': Region.objects.get(region_id=district['REGION']),
            'data': {
                'name': fast_match['District Name'],
                'tea_id': district['DISTRICT'],
                'street': ccd_match['LSTREE'],
                'city': ccd_match['LCITY'],
                'state': ccd_match['LSTATE'],
                'zip_code': zip_code,
                'latitude': ccd_match['LATCOD'],
                'longitude': ccd_match['LONCOD'],
            }
        }

    def create_district(self, district):
        data = self.reformat_data(district)
        form = DistrictAddForm(data['data'])

        if form.is_valid():
            district_instance = form.save(commit=False)
            district_instance.county = data['county']
            district_instance.region = data['region']
            district_instance.save()
            self.count += 1
        else:
            self.errors.append(form.errors)
