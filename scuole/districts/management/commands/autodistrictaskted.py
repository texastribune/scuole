# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os
import string
import requests

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Update AskTED data every day!'

    def handle(self, *args, **options):
        self.load_askted_superintendent_csv()

    def load_askted_superintendent_csv(self):
        url = 'http://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx'
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

        askted_update = os.path.join(
            settings.DATA_FOLDER,
            'askted', 'district')

        with open(askted_update + '/askted_update.csv', 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in reader:
                writer.writerow(row)
                # print(row['District Name'])

        # incorporate loading data into models here
        # no need to push to new file yet, maybe if we want to archive
        # later
