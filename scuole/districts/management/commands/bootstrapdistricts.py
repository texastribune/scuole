# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Count
from django.utils.text import slugify

from scuole.core.utils import massage_name
from scuole.core.replacements import ISD_REPLACEMENT

from scuole.counties.models import County
from scuole.regions.models import Region

from ...models import District


class Command(BaseCommand):
    help = 'Bootstraps District models using TEA and CCD data.'

    def handle(self, *args, **options):
        ccd_file_location = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-districts-ccd.csv')

        self.ccd_data = self.load_ccd_file(ccd_file_location)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', '2013-14', 'district', 'district-reference.csv')

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            districts = []

            for row in reader:
                districts.append(self.create_district(row))

            District.objects.bulk_create(districts)
            self.dedupe_districts()

    def load_ccd_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row['STID']] = row

        return payload

    def create_district(self, district):
        ccd_match = self.ccd_data[district['DISTRICT']]
        name = massage_name(ccd_match['NAME'], ISD_REPLACEMENT)
        county = County.objects.get(fips=ccd_match['CONUM'][-3:])
        slug = slugify(name)

        self.stdout.write('Creating {}...'.format(name))

        return District(
            name=name,
            slug=slug,
            tea_id=district['DISTRICT'],
            street=ccd_match['LSTREE'],
            city=ccd_match['LCITY'],
            state=ccd_match['LSTATE'],
            zip_code=ccd_match['LZIP'],
            zip_code4=ccd_match['LZIP4'],
            latitude=ccd_match['LATCOD'],
            longitude=ccd_match['LONCOD'],
            region=Region.objects.get(region_id=district['REGION']),
            county=county,
        )

    def dedupe_districts(self):
        dupes = District.objects.values(
            'name', 'slug').annotate(
            Count('slug')).values('name').filter(slug__count__gt=1)

        for district in District.objects.filter(name__in=dupes):
            self.stdout.write('Deduping {name} in {county} County...'.format(
                name=district.name,
                county=district.county.name
            ))

            district.slug = slugify('{name} {county}'.format(
                name=district.name,
                county=district.county.name
            ))

            district.name = '{name} ({county} County)'.format(
                name=district.name,
                county=district.county.name
            )

            district.save()
