# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from scuole.states.models import State, Commissioner


class Command(BaseCommand):
    help = 'Bootstraps state models.'

    def handle(self, *args, **options):
        self.create_state()

        commissioner_csv = os.path.join(
            settings.DATA_FOLDER,
            'state', 'state.csv')

        self.commissioner_data = self.load_commissioner_file(
            commissioner_csv)

        commissioner = self.commissioner_data
        self.load_commissioner(commissioner)

    def load_commissioner_file(self, file):
        payload = {}

        with open(file, 'rU') as f:
            reader = csv.DictReader(f)

            for row in reader:
                texas = row['Full Name']
                payload[texas] = row

        return payload

    def create_state(self):
        self.stdout.write('Creating Texas...')

        State.objects.update_or_create(
            defaults={
                'name': 'TX',
                'slug': 'tx',
            }
        )

    def load_commissioner(self, commissioner):
        Commissioner.objects.update_or_create(
            defaults={
                'name': 'Full Name',
                'role': 'Role',
                'email': 'Email',
                'phone_number': 'Phone',
                'fax_number': 'Fax',
            }
        )
