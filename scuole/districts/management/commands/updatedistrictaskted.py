# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string


from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Update AskTED data.'

    def handle(self, *args, **options):
        # path to askted master directory file
        askted_csv = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')
        # path to superintendent personell file
        superintendent_csv = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district', 'superintendents.csv')

        # call load function on superintendent file
        self.superintendent_data = self.load_superintendent_file(
            superintendent_csv)

        # loops through each row in askted directory to update district  models
        with open(askted_csv) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.update_district(row)

    # loops through each row in superintendent file to create superintendent model
    def load_superintendent_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['District Number'].replace("'", "")
                payload[tea_id] = row

        return payload

    def update_district(self, district):
        # askTed districts have apostrophes in them
        district_id = str(district['District Number']).replace("'", "")
        district_name = district['District Name']

        # if there's a district already in the databasa, match this askTed data
        # to that TAPR data. Otherwise, move on
        try:
            district_match = District.objects.get(tea_id=district_id)

            phone_number = district['District Phone']
            fax_number = district['District Fax']
            # sometimes phone and fax numbers have extensions at the end
            # this splits out the extension into its own field
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

            # update all of the askTed district fields and save it to the model
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

            superintendent = self.superintendent_data[district_id]
            self.create_superintendent(district_match, superintendent)

            self.stdout.write('Creating {}...'.format(district_name))
        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(district_name))

    def create_superintendent(self, district, superintendent):

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
        # unlike the district model we're updating above, the superintendent
        # model doesn't exist yet- so we're creating it here
        instance, _ = Superintendent.objects.update_or_create(
            name=name,
            district=district,
            defaults={
                'role': superintendent['Role'],
                'email': superintendent['Email Address'],
                'phone_number': phone_number,
                'phone_number_extension': phone_number_extension,
                'fax_number': fax_number,
                'fax_number_extension': fax_number_extension,
            }
        )
