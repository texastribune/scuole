# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from ...models import Campus, Principal


class Command(BaseCommand):
    help = 'Update AskTED data.'

    def handle(self, *args, **options):
        # path to askted master directory file
        askted_csv = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        # path to principal askted personell file
        principal_file = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'campus', 'principals.csv')

        # calls function that loads principal file on principal data
        self.principals_data = self.load_principal_file(
            principal_file)

        # loops through each row in directory to update campus model
        with open(askted_csv) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.update_campus(row)

    # loops through each row in principal file to create principal file
    def load_principal_file(self, file):
        payload = {}

        with open(file, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['Organization Number'].replace("'", "")

                if tea_id not in payload:
                    payload[tea_id] = []

                payload[tea_id].append(row)

        return payload

    def update_campus(self, campus):
        # askted IDs have apostrophes in them
        campus_id = str(campus['School Number']).replace("'", "")
        campus_name = campus['School Name']
        # if the campus exists in TAPR data, proceed updating its askTed fields
        # otherwise skip it
        try:
            campus_match = Campus.objects.get(tea_id=campus_id)

            phone_number = campus['School Phone']
            fax_number = campus['School Fax']
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

            # update all of the askTed campus fields and save it to the model
            campus_match.phone_number = phone_number
            campus_match.phone_number_extension = phone_number_extension
            campus_match.fax_number = fax_number
            campus_match.fax_number_extension = fax_number_extension
            campus_match.street = campus['School Street Address']
            campus_match.city = campus['School City']
            campus_match.state = campus['School State']
            campus_match.zip_code = campus['School Zip']
            campus_match.website = campus['School Web Page Address']
            campus_match.save()

            principals_campus_id = str(campus['School Number']).replace("'", "")
            principals = self.principals_data[
                principals_campus_id]
            self.create_principals(campus_match, principals)

            self.stdout.write('Creating {}...'.format(campus_name))
        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(campus_name))

    # unlike the campus model we're updating above, the principal model doesn't
    # exist yet- so we're creating it here
    def create_principals(self, campus, principals):
        for principal in principals:
            name = '{} {}'.format(
                principal['First Name'], principal['Last Name'])
            name = string.capwords(name)
            phone_number = principal['Phone']
            fax_number = principal['Fax']

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

            instance, _ = Principal.objects.update_or_create(
                name=name,
                campus=campus,
                defaults={
                    'role': principal['Role'],
                    'email': principal['Email Address'],
                    'phone_number': phone_number,
                    'phone_number_extension': phone_number_extension,
                    'fax_number': fax_number,
                    'fax_number_extension': fax_number_extension,
                }
            )
