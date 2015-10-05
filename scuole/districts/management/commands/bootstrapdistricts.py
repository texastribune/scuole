# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.geos import GEOSGeometry, Point

from scuole.core.utils import remove_charter_c
from scuole.counties.models import County
from scuole.regions.models import Region

from ...models import District

from slugify import slugify


class Command(BaseCommand):
    help = 'Bootstraps District models using TEA, FAST and CCD data.'

    def handle(self, *args, **options):
        ccd_file_location = os.path.join(
            settings.DATA_FOLDER, 'ccd', 'tx-districts-ccd.csv')

        self.ccd_data = self.load_ccd_file(ccd_file_location)

        fast_file_location = os.path.join(
            settings.DATA_FOLDER, 'fast', 'fast-district.csv')

        self.fast_data = self.load_fast_file(fast_file_location)

        district_shp = os.path.abspath(os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'shapes', 'SchoolDistricts.shp'))

        self.shape_data = self.load_shape_file(district_shp)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            'tapr', 'reference', 'district', 'reference.csv')

        with open(tea_file, 'r') as f:
            reader = csv.DictReader(f)

            districts = []

            for row in reader:
                districts.append(self.create_district(row))

            District.objects.bulk_create(districts)

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

    def load_shape_file(self, file):
        district_mapping = {
            'tea_id' : 'OBJECTID',
            'mpoly' : 'SDA10',
            'name' : 'NAME',
            'name2' : 'NAME2',
            'districtn' : 'DISTRICT_N',
            'district': 'DISTRICT',
            'districtc' : 'DISTRICT_C',
            'ncesDistrict' : 'NCES_DISTRICT',
            'color' : 'COLOR',
            'color2' : 'COLOR2',
            'shapeLen' : 'Shape_Leng',
            'shapeArea': 'Shape_Area',
        }

        def run(verbose=True):
            lm = LayerMapping(District, district_shp, district_mapping,
                              transform=False, encoding='iso-8859-1')

            lm.save(strict=True, verbose=verbose, fid_range=(0,1))

    def create_district(self, district):
        ccd_match = self.ccd_data[district['DISTRICT']]
        fast_match = self.fast_data[str(int(district['DISTRICT']))]
        shape_match = self.shape_data
        self.stdout.write('Creating {}...'.format(fast_match['District Name']))
        name = remove_charter_c(fast_match['District Name'])
        county = County.objects.get(fips=ccd_match['CONUM'][-3:])
        pnt = Point(float(ccd_match['LONCOD']), float(ccd_match['LATCOD']))


        return District(
            name=name,
            slug=slugify(name),
            tea_id=district['DISTRICT'],
            street=ccd_match['LSTREE'],
            city=ccd_match['LCITY'],
            state=ccd_match['LSTATE'],
            zip_code='{LZIP}-{LZIP4}'.format(
                LZIP=ccd_match['LZIP'],
                LZIP4=ccd_match['LZIP4']),
            latitude=ccd_match['LATCOD'],
            longitude=ccd_match['LONCOD'],
            latlong=pnt,
            region=Region.objects.get(region_id=district['REGION']),
            county=county,
            mpoly=shape_match,
        )
