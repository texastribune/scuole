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

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Update AskTED data.'

    def handle(self, *args, **options):
        askted_csv = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        # self.askted_data = self.load_askted_file(askted_file_location)

        superintendent_csv = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district', 'superintendents.csv')

        self.superintendent_data = self.load_superintendent_file(
            superintendent_csv)

        with open(askted_csv) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.update_district(row)

    def load_superintendent_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['District Number'].replace("'", "")
                payload[tea_id] = row

        return payload

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

            print(district_name)

            if district['District Number'] in self.superintendent_data:
                superintendent = self.superintendent_data[
                    district['District Number']]
                self.load_superintendent(district_match, superintendent)
            else:
                self.stderr.write('No superintendent data for {}'.format(district_name))

        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(district_name))

    def create_superintendent(self, district, superintendent):
        district_id = str(superintendent['District Number']).replace("'", "")
        district_name = str(superintendent['District Name'])
        # district_tea = District.objects.get(tea_id=district_id)

        name = '{} {}'.format(
            superintendent['First Name'], superintendent['Last Name'])
        name = string.capwords(name)
        phone_number = superintendent['Phone']
        fax_number = superintendent['Fax']

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


        s = Superintendent.objects.get(district__tea_id=district_id)
        print(s)

        # Superintendent.district = district
        # Superintendent.role = superintendent['Role']
        # Superintendent.email = superintendent['Email Address']
        # Superintendent.phone_number = phone_number
        # Superintendent.phone_number_extension = phone_number_extension
        # Superintendent.fax_number = fax_number
        # Superintendent.fax_number_extension = fax_number_extension
        # Superintendent.save()

        print(district_name)



