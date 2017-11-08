# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
# import json
import os
import string

# from slugify import slugify

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import Count
# from django.contrib.gis.geos import GEOSGeometry, MultiPolygon

# from scuole.core.utils import remove_charter_c
# from scuole.counties.models import County
# from scuole.regions.models import Region

from ...models import District, Superintendent

# from scuole.core.replacements import ISD_REPLACEMENT
# from scuole.core.utils import massage_name


class Command(BaseCommand):
    help = 'Update AskTED data.'

    def handle(self, *args, **options):
        askted_csv = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        # self.askted_data = self.load_askted_file(askted_file_location)

        superintendent_csv = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district', 'superintendents.csv')

        # self.superintendent_data = self.load_superintendent_file(
        #     superintendent_csv)

        with open(askted_csv) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.update_district(row)

    # def load_askted_file(self, file):
    #     payload = {}

    #     with open(file, 'rU') as f:
    #         reader = csv.DictReader(f)

    #         for row in reader:
    #             tea_id = row['District Number'].replace("'", "")
    #             payload[tea_id] = row

    #     return payload

    def update_district(self, district):
        district_id = str(district['District Number']).replace("'", "")
        district_name = district['District Name']

        try:
            district_match = District.objects.get(tea_id=district_id)

            phone_number = district['District Phone']
            fax_number = district['District Fax']

            if 'ext' in phone_number:
                phone_number, phone_number_extension = phone_number.split(' ext:')
                phone_number_extension = str(phone_number_extension)
            else:
                phone_number_extension = ''

            if 'ext' in fax_number:
                fax_number, fax_number_extension = fax_number.split(' ext:')
                fax_number_extension = str(phone_number_extension)
            else:
                fax_number_extension = ''

            district_match.phone_number = phone_number
            district_match.phone_number_extension = phone_number_extension
            district_match.fax_number = fax_number
            district_match.fax_number_extension = fax_number_extension
            district_match.street = district['District Street Address']
            district_match.city = district['District City']
            district_match.state = district['District State']
            district_match.zip_code = district['District Zip']
            district_match.website = district['District Web Page Address']
            district_match.save()

            print(district_match.name)
        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(district_name))

    # def update_superintendent(self, superintendent):
    #     district_id = str(superintendent['District Number']).replace("'", "")
    #     district_name = str(superintendent['District Name'])
    #     try:
    #         # district_tea = District.objects.get(tea_id=district_id)
    #         Superintendent.objects.filter(district__tea_id=district_id).update(name=superintendent['Full Name'])

    #         name = '{} {}'.format(
    #             superintendent['First Name'], superintendent['Last Name'])
    #         name = string.capwords(name)
    #         phone_number = superintendent['Phone']
    #         fax_number = superintendent['Fax']

    #         if 'ext' in phone_number:
    #             phone_number, phone_number_extension = phone_number.split(' ext:')
    #             phone_number_extension = str(phone_number_extension)
    #         else:
    #             phone_number_extension = ''

    #         if 'ext' in fax_number:
    #             fax_number, fax_number_extension = fax_number.split(' ext:')
    #             fax_number_extension = str(phone_number_extension)
    #         else:
    #             fax_number_extension = ''

    #         instance, _ = Superintendent.objects.upate_or_create(
    #             name=name,
    #             district=district,
    #             defaults={
    #                 'role': string.capwords(superintendent['Role']),
    #                 'email': superintendent['Email Address'],
    #                 'phone_number': phone_number,
    #                 'phone_number_extension': phone_number_extension,
    #                 'fax_number': fax_number,
    #                 'fax_number_extension': fax_number_extension,
    #             })

    #     except ObjectDoesNotExist:
    #         self.stderr.write('No askted data for {}'.format(district_name))

    #     print(district_name)


