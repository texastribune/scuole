# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string
import requests
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Update AskTED data every day!'

    def handle(self, *args, **options):
        askted_folder = os.path.join(
            settings.DATA_FOLDER,
            'askted')

        district_folder = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district')

        self.load_askted_directory_csv(askted_folder)
        self.load_superintendent_directory_csv(district_folder)

    def load_askted_directory_csv(self, file):
        url = 'http://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile.aspx'
        payload = {
            '_VIEWSTATE':'',
            '__VIEWSTATEGENERATOR':'44F2C40C',
            'ddlSortOrder':'School+Number',
            'btnDownloadFile':'Download+File'
        }

        req = requests.post(url, data=payload)
        reader = csv.DictReader(req.text.splitlines())
        date = str(datetime.datetime.now().date())
        directoryFilename = file + '/' + date + '_askTedDirectory.csv'
        isDirectoryFile = os.path.isfile(directoryFilename)

        def createNewDistrictFile():
            with open(directoryFilename, 'w+') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                print(writer)
                for row in reader:
                    writer.writerow(row)
                    # print(row['District Name'])

        if not isDirectoryFile:
            createNewDistrictFile()
        else:
            print("there's already a file here!")

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

        req = requests.post(url, data=data)
        reader = csv.DictReader(req.text.splitlines())
        date = str(datetime.datetime.now().date())
        superintendentFilename = file + '/' + date + '_askTedSuperindendent.csv'
        isSuperintendentFile = os.path.isfile(superintendentFilename)

        def createNewSuptFile():
            with open(superintendentFilename, 'w+') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                print(writer)
                for row in reader:
                    writer.writerow(row)
                    # print(row['District Name'])

        if not isSuperintendentFile:
            createNewSuptFile()
        else:
            print("there's already a file here!")


        # incorporate loading data into models here
        # no need to push to new file yet, maybe if we want to archive
        # later
