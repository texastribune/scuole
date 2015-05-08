# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from ...models import District


class Command(BaseCommand):
    help = 'Bootstraps District models using CCD data.'

    def handle(self, *args, **options):
        districts_file = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-districts-ccd.csv')

        with open(districts_file, 'rb') as f:
            reader = csv.DictReader(f)

            districts = []

            for row in reader:
                districts.append(self.create_district(row))

            District.objects.bulk_create(districts)

    def create_district(self, district):
        return District(
            name=district['NAME'],
            slug=slugify(district['NAME']),
            tea_id=district['STID'],
            street=district['LSTREE'],
            city=district['LCITY'],
            state=district['LSTATE'],
            zip_code=district['LZIP'],
            zip_code4=district['LZIP4'],
            latitude=district['LATCOD'],
            longitude=district['LONCOD'],
        )
