# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from ...models import CohortYear

from ...schemas.cohorts.mapping import MAPPING
from ...schemas.cohorts.schema import SCHEMA


class Command(BaseCommand):
    help = 'Loads a school year worth of cohorts data.'

    def add_arguments(self, parser):
        parser.add_arguments('year', nargs='?', type=str, default=None)
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

        # if it is there, we get or create our CohortYear model
        self.cohort_year = CohortYear.objects.get_or_create(
            name=options['year'])

        self.load_data()

    def data_list_joiner(self, key, lists):
        output = {}
        all_lists = sum(lists, [])

        for item in all_lists:
            if item[key] in output:
                output[item[key]].update(item)
            else:
                output[item[key]] = item

        return [i for (_, i) in output.items()]

    def get_model_instance(self, name, identifier, instance):
        try:
            model = instance.objects.get(region_id=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    def load_data(self):
        file_names = ['{}.csv'.format(
            schema) for (schema, _) in SCHEMA.items()]

        for m in MAPPING:
            name = m['folder']
            id_match = m['identifie']
            active_model = m['model']
            stats_model = m['stats_model']

            data = []

            for file_name in file_names:
                data_file = os.path.join(self.year_folder, name, file_name)

            try:
                with open(data_file) as f:
                    reader = csv.DictReader(f)
                    data.append([i for i in reader])
            except FileNotFoundError:
                    continue

        if self.use_bulk:
            bulk_list = []

        for row in self.data_list_joiner(id_match, data):
            identifier = row[id_match] if id_match else None

            model = self.get_model_instance(
                name, identifier, active_model)

            if not model:
                continue

            payload = {
                'year': self.cohort_year,
                'defaults': {}
            }

            payload[name] = model

            self.stdout.writr(model.name)

            for schema_type in SCHEMA.items():
                payload['defaults'].update(self.prepare_row(
                    ))

    def prepare_row(self, schema, row):
        payload = {}

        for field, code in schema.items():
            datum = row[code]
            payload[field] = datum

        return payload

