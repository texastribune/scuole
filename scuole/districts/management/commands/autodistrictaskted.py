# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import datetime
import os
import requests
import string

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Update AskTED data every day!'

    def handle(self, *args, **options):
        askted_folder = os.path.join(
            settings.DATA_FOLDER, 'askted')

        district_folder = os.path.join(
            settings.DATA_FOLDER, 'askted', 'district')

        self.superintendent_data = self.load_superintendent_directory_csv(
            district_folder)

        self.load_askted_directory_csv(askted_folder)

    def load_askted_directory_csv(self, directory):
        url = 'http://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile.aspx'
        data = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '44F2C40C',
            'ddlSortOrder': 'School+Number',
            'btnDownloadFile': 'Download+File',
        }

        req = requests.post(url, data=data)
        reader = csv.DictReader(req.text.splitlines())
        fieldnames = [
            'School Name',
            'Instruction Type',
            'School State',
            'District Superintendent',
            'School Status Date',
            'School Email Address',
            'School Number',
            'Region Number',
            'County Number',
            'County Name',
            'District Email Address',
            'District Number',
            'Update Date',
            'District City',
            'School Enrollment as of Oct 2016',
            'School Zip',
            'School Principal',
            'School Fax',
            'District Web Page Address',
            'District Street Address',
            'District Fax',
            'School Phone',
            'District Enrollment as of Oct 2016',
            'Grade Range',
            'School Status',
            'District Name',
            'School Web Page Address',
            'School Street Address',
            'District Zip',
            'District State',
            'District Type',
            'Charter Type',
            'District Phone',
            'School City',
        ]

        date = str(datetime.datetime.now().date())
        directoryFilename = directory + '/' + date + '_askTedDirectory.csv'
        directoryFile = os.path.join(
            settings.DATA_FOLDER, 'askted', date + '_askTedDirectory.csv')
        isDirectoryFile = os.path.isfile(directoryFilename)

        if not isDirectoryFile:
            with open(directoryFilename, 'w+') as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
        else:
            print("We already have today's district data! Moving on...")

        with open(directoryFile, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.update_district(row)

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

            self.stdout.write('Updating {}...'.format(district_name))
        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(district_name))

    def load_superintendent_directory_csv(self, file):
        # url where general directory lives
        url = 'http://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx'
        # request params
        data = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '3B1DF71D',
            'chkSuper': 'on',
            'lstDistrictStaff': '0',
            'lstESCStaff': '0',
            'ddlSortOrder': 'Organization+Name',
            'btnDownloadFile': 'Download+File',
        }
        fieldnames = [
            'Charter Type',
            'Email Address',
            'Organization Name',
            'Full Name',
            'Role',
            'Fax',
            'State',
            'District Name',
            'Organization Number',
            'First Name',
            'Last Name',
            'Organization SubType',
            'County Number',
            'Street Address',
            'Zip',
            'Region Number',
            'Salutation Title',
            'Phone',
            'Organization Type',
            'County Name',
            'City',
            'District Number',
        ]
        req = requests.post(url, data=data)
        reader = csv.DictReader(req.text.splitlines())

        payload = {}

        for row in reader:
            tea_id = row['District Number'].replace("'", "")
            payload[tea_id] = row

        return payload

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

        self.stdout.write('Creating Superintendent {} from {}...'.format(name, district))
