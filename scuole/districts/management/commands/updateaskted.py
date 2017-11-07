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
        askted_file_location = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        self.askted_data = self.load_askted_file(askted_file_location)

        superintendent_csv = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district', 'superintendents.csv')

        # self.superintendent_data = self.load_superintendent_file(
        #     superintendent_csv)

        with open(superintendent_csv) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.update_district(row)

    def load_askted_file(self, file):
        payload = {}

        with open(file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['District Number'].replace("'", "")
                payload[tea_id] = row

        return payload

    def update_district(self, district):
        district_id = str(district['District Number']).replace("'", "")
        district_name = str(district['District Name'])
        try:
            district = District.objects.get(tea_id=district_id)
            district.phone_number = district['District Phone']
            district.zipcode = district['District ']
        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(district_name))

        print(district_name)




    #     if district['DISTRICT'] in self.askted_data:
    #         askted_match = self.askted_data[district['DISTRICT']]
    #         phone_number = askted_match['District Phone']
    #         if 'ext' in phone_number:
    #             phone_number, phone_number_extension = phone_number.split(
    #                 ' ext:')
    #             phone_number_extension = str(phone_number_extension)
    #         else:
    #             phone_number_extension = ''
    #         street = askted_match['District Street Address']
    #         city = askted_match['District City']
    #         state = askted_match['District State']
    #         zip_code = askted_match['District Zip']
    #         website = askted_match['District Web Page Address']
    #     else:
    #         self.stderr.write('No askted data for {}'.format(name))
    #         phone_number = ''
    #         phone_number_extension = ''
    #         street = ''
    #         city = ''
    #         state = ''
    #         zip_code = ''
    #         website = ''

    #     instance, _ = District.objects.update_or_create(
    #         tea_id=district['DISTRICT'],
    #         defaults={
    #             'phone_number': phone_number,
    #             'phone_number_extension': phone_number_extension,
    #             'website': website,
    #             'street': street,
    #             'city': city,
    #             'state': state,
    #             'zip_code': zip_code,
    #         }
    #     )

    #     if district['DISTRICT'] in self.superintendent_data:
    #         superintendent = self.superintendent_data[
    #             district['DISTRICT']]
    #         self.load_superintendent(instance, superintendent)
    #     else:
    #         self.stderr.write('No superintendent data for {}'.format(name))

    # def load_superintendent(self, district, superintendent):
    #     name = '{} {}'.format(
    #         superintendent['First Name'], superintendent['Last Name'])
    #     name = string.capwords(name)
    #     phone_number = superintendent['Phone']
    #     fax_number = superintendent['Fax']

    #     if 'ext' in phone_number:
    #         phone_number, phone_number_extension = phone_number.split(' ext:')
    #         phone_number_extension = str(phone_number_extension)
    #     else:
    #         phone_number_extension = ''

    #     if 'ext' in fax_number:
    #         fax_number, fax_number_extension = fax_number.split(' ext:')
    #         fax_number_extension = str(phone_number_extension)
    #     else:
    #         fax_number_extension = ''

    #     Superintendent.objects.update_or_create(
    #         name=name,
    #         district=district,
    #         defaults={
    #             'role': string.capwords(superintendent['Role']),
    #             'email': superintendent['Email Address'],
    #             'phone_number': phone_number,
    #             'phone_number_extension': phone_number_extension,
    #             'fax_number': fax_number,
    #             'fax_number_extension': fax_number_extension,
    #         }
    #     )
