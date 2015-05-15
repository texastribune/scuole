# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from scuole.districts.models import District

from ...models import Campus


class Command(BaseCommand):
    help = 'Bootstraps Campus models using TEA and CCD data.'

    def handle(self, *args, **options):
        ccd_file_location = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-campuses-ccd.csv')

        self.ccd_data = self.load_ccd_file(ccd_file_location)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', '2013-14', 'campus', 'campus-reference.csv')

        with open(tea_file, 'rb') as f:
            reader = csv.DictReader(f)

            campuses = []

            for row in reader:
                campuses.append(self.create_campus(row))

            Campus.objects.bulk_create(campuses)

    def load_ccd_file(self, file):
        payload = {}

        with open(file, 'rb') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['SEASCH']] = row

        return payload

    def create_campus(self, campus):
        ccd_match = self.ccd_data[campus['CAMPUS']]
        self.stdout.write('Creating {}...'.format(ccd_match['SCHNAM']))

        return Campus(
            name=ccd_match['SCHNAM'],
            slug=slugify(ccd_match['SCHNAM']),
            tea_id=campus['CAMPUS'],
            phone=ccd_match['PHONE'],
            street=ccd_match['LSTREE'],
            city=ccd_match['LCITY'],
            state=ccd_match['LSTATE'],
            zip_code=ccd_match['LZIP'],
            zip_code4=ccd_match['LZIP4'],
            locale=ccd_match['ULOCAL'],
            latitude=ccd_match['LATCOD'],
            longitude=ccd_match['LONCOD'],
            district=District.objects.get(tea_id=campus['DISTRICT']),
        )
