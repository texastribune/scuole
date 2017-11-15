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

from ...models import District, Campus, Principal


class Command(BaseCommand):
    help = 'Update AskTED data.'

    def handle(self, *args, **options):
        askted_csv = os.path.join(
            settings.DATA_FOLDER, 'askted', 'directory.csv')

        # self.askted_data = self.load_askted_file(askted_file_location)

        principal_file = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'campus', 'principals.csv')

        self.principals_data = self.load_principal_file(
            principal_file)

        with open(askted_csv) as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.update_campus(row)

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
        campus_id = str(campus['School Number']).replace("'", "")
        campus_name = campus['School Name']

        try:
            campus_match = Campus.objects.get(tea_id=campus_id)

            phone_number = campus['School Phone']
            fax_number = campus['School Fax']

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
