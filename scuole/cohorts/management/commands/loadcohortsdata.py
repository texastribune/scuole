# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from scuole.states.models import State
from ...models import CohortsYear

from ...schemas.cohorts.mapping import MAPPING
from ...schemas.cohorts.schema import SCHEMA


class Command(BaseCommand):
    help = 'Loads a school year worth of cohorts data.'

    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)
        parser.add_argument('--bulk', action='store_true')

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

        self.use_bulk = options['bulk']

        # get cohorts folder
        cohorts_folder = os.path.join(settings.DATA_FOLDER, 'cohorts')

        # make sure year passed in actually has folder
        self.year_folder = os.path.join(cohorts_folder, options['year'])

        if not os.path.isdir(self.year_folder):
            raise CommandError(
                '`{}` was not found in your cohorts data directory'.format(
                    self.year_folder))

        # if it is there, we get or create our CohortsYear model
        self.cohorts_year = CohortsYear.objects.get_or_create(
            name=options['year'])

        self.load_data()

    def data_list_joiner(self, key, lists):
        output = {}

        if key:
            all_lists = sum(lists, [])

            for item in all_lists:
                if item[key] in output:
                    output[item[key]].update(item)
                else:
                    output[item[key]] = item
        else:
            output['STATE'] = {}

            for d in lists:
                output['STATE'].update(d[0])

        return [i for (_, i) in output.items()]

    def get_model_instance(self, name, identifier, instance):
        # name is a parameter set in the mapping.py file that
        # I set this manually as state or region
        if name == 'state':
            return State.objects.get(name='TX')

        if name == 'region':
            return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    def load_data(self):
        # Finds the file based on what the schema dict is called
        file_names = ['{}.csv'.format(
            schema) for (schema, _) in SCHEMA.items()]

        for m in MAPPING:
            name = m['folder']
            id_match = m['identifier']
            active_model = m['model']
            cohorts_model = m['cohorts_model']

            data = []
            # For now we only have one file in the schema, but we'll need
            # more when we start introducing counties
            for file_name in file_names:
                data_file = os.path.join(self.year_folder, file_name)
                # Grabs the data in the file and adds it to the data list
                try:
                    with open(data_file) as f:
                        reader = csv.DictReader(f)
                        data.append([i for i in reader])
                except FileNotFoundError:
                    continue

            if self.use_bulk:
                bulk_list = []

            # loops through each row in the data file and updates or
            # creates a model based on the identifier listed in the
            # mapping.py file. Regions are identified by their
            # 'Region Code' in the spreadsheet. If a row doesn't have a
            # 'Region Code', then it's state data.
            for row in self.data_list_joiner(id_match, data):
                identifier = row[id_match] if id_match else None

                model = self.get_model_instance(
                    name, identifier, active_model)

                if not model:
                    continue

                # help what's a payload
                payload = {
                    'year': self.cohorts_year,
                    'defaults': {}
                }

                payload[name] = model

                self.stdout.write(model.name)

                for schema_type, schema in SCHEMA.items():
                    payload['defaults'].update(self.prepare_row(
                        schema, row))
                # This is where I get lost. I don't know what new_payload
                # does or means other than it creates the model.
                if not self.use_bulk:
                    cohorts_model.objects.update_or_create(**payload)
                else:
                    new_payload = payload['defaults']
                    new_payload['year'] = payload['year']
                    new_payload[name] = payload[name]

                    # I get an error here saying:
                    # TypeError: 'state' is an invalid keyword argument
                    # for this function
                    bulk_list.append(cohorts_model(**new_payload))

            cohorts_model.objects.bulk_create(bulk_list)

    # For the stats loader, this was used to create the weird column headers
    # that had different suffixes and prefixes based on the year, whether
    # it was a count or percent, and whether it was for state, region county,
    # district or campus. We don't need these as much here- so this just
    # matches fields with schema names and codes used in the spreadsheet
    def prepare_row(self, schema, row):
        payload = {}

        for field, code in schema.items():
            datum = row[code]
            payload[field] = datum

        return payload
