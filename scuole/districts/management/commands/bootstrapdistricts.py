# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from ...models import District
from scuole.regions.models import Region


class Command(BaseCommand):
    help = 'Bootstraps District models using TEA and CCD data.'

    def handle(self, *args, **options):
        ccd_file_location = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-districts-ccd.csv')

        self.ccd_data = self.load_ccd_file(ccd_file_location)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', '2013-14', 'district', 'district-reference.csv')

        with open(tea_file, 'rb') as f:
            reader = csv.DictReader(f)

            districts = []

            for row in reader:
                districts.append(self.create_district(row))

            District.objects.bulk_create(districts)

    def load_ccd_file(self, file):
        payload = {}

        with open(file, 'rb') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['STID']] = row

        return payload

    def create_district(self, district):
        ccd_match = self.ccd_data[district['DISTRICT']]

        return District(
            name=ccd_match['NAME'],
            slug=slugify(ccd_match['NAME']),
            tea_id=district['DISTRICT'],
            street=ccd_match['LSTREE'],
            city=ccd_match['LCITY'],
            state=ccd_match['LSTATE'],
            zip_code=ccd_match['LZIP'],
            zip_code4=ccd_match['LZIP4'],
            latitude=ccd_match['LATCOD'],
            longitude=ccd_match['LONCOD'],
            region=Region.objects.get(region_id=district['REGION']),
        )
