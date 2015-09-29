# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from scuole.states.models import State
from ...models import SchoolYear

from ...schemas.tapr.mapping import MAPPING
from ...schemas.tapr.schema import SCHEMA


class Command(BaseCommand):
    help = 'Loads a school year worth of TAPR data.'

    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

        # get the base TAPR folder
        tapr_folder = os.path.join(settings.DATA_FOLDER, 'tapr')

        # make sure the `year` passed in actually has a folder
        self.year_folder = os.path.join(tapr_folder, options['year'])

        if not os.path.isdir(self.year_folder):
            raise CommandError(
                '`{}` was not found in your TAPR data directory'.format(
                    self.year_folder))

        # if it is there, we get or create the SchoolYear model
        self.school_year, _ = SchoolYear.objects.get_or_create(
            name=options['year'])

        self.load_data()

    def get_model_instance(self, name, identifier, instance):
        if name == 'state':
            return State.objects.get(name='TX')

        if name == 'region':
            return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(tea_id=identifier)
        except instance.DoesNotExist:
            self.stdout.write('Could not find {}'.format(identifier))
            return None

        return model

    def load_data(self):
        for m in MAPPING:
            name = m['folder']
            id_match = m['identifier']
            active_model = m['model']
            stats_model = m['stats_model']

            # Loop through all the field mappings
            for schema, values in SCHEMA.items():
                file_name = '{}.csv'.format(schema)
                data_file = os.path.join(self.year_folder, name, file_name)

                with open(data_file) as f:
                    reader = csv.DictReader(f)

                    for row in reader:
                        identifier = row[id_match] if id_match else None

                        model = self.get_model_instance(
                            name, identifier, active_model)

                        if not model:
                            continue

                        payload = {
                            'year': self.school_year,
                            'defaults': {}
                        }

                        payload[name] = model

                        self.stdout.write(model.name)

                        if schema == 'staff-and-student-information':
                            payload['defaults'].update(
                                self.load_staff_students(
                                    m['short_code'], values, row))
                        if schema == ('postsecondary-readiness-and-'
                                      'non-staar-performance-indicators'):
                            payload['defaults'].update(
                                self.load_postsecondary_readiness(
                                    m['short_code'], values, row))

                        stats_model.objects.update_or_create(**payload)

    def load_staff_students(self, short_code, schema, row):
        payload = {}

        for field, code in schema.items():
            datum = row[short_code + code]

            if datum == '.':
                datum = None

            payload[field] = datum

        return payload

    def load_postsecondary_readiness(self, short_code, schema, row):
        payload = {}

        short_year = self.school_year.name.split('-')[0][2:]

        for field, code in schema.items():
            if 'count' in field:
                suffix = 'D'
            elif 'percent' in field or 'rate' in field or 'avg' in field:
                suffix = 'R'

            datum = row[short_code + code + short_year + suffix]

            if datum == '.':
                datum = None

            payload[field] = datum

        return payload
