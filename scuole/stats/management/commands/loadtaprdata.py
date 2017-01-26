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
        parser.add_argument('--bulk', action='store_true')

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

        self.use_bulk = options['bulk']

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
        if name == 'state':
            return State.objects.get(name='TX')

        if name == 'region':
            return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(tea_id=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    def load_data(self):
        file_names = ['{}.csv'.format(
            schema) for (schema, _) in SCHEMA.items()]

        no_reference_file = ('state', 'region')

        for m in MAPPING:
            name = m['folder']
            id_match = m['identifier']
            active_model = m['model']
            stats_model = m['stats_model']

            data = []

            for file_name in file_names:
                if name in no_reference_file and file_name == 'reference.csv':
                    continue
                data_file = os.path.join(self.year_folder, name, file_name)

                with open(data_file, 'rU') as f:
                    reader = csv.DictReader(f)
                    data.append([i for i in reader])

            if self.use_bulk:
                bulk_list = []

            for row in self.data_list_joiner(id_match, data):
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

                for schema_type, schema in SCHEMA.items():
                    if (name in no_reference_file
                            and schema_type == 'reference'):
                        continue
                    payload['defaults'].update(self.prepare_row(
                        m['short_code'], schema_type, schema, row))

                if not self.use_bulk:
                    stats_model.objects.update_or_create(**payload)
                else:
                    new_payload = payload['defaults']
                    new_payload['year'] = payload['year']
                    new_payload[name] = payload[name]

                    bulk_list.append(stats_model(**new_payload))

            stats_model.objects.bulk_create(bulk_list)

    def prepare_row(self, short_code, schema_type, schema, row):
        payload = {}

        short_year = self.school_year.name.split('-')[0][2:]

        for field, code in schema.items():
            if schema_type == ('postsecondary-readiness-and-non-staar-'
                               'performance-indicators') or schema_type == (
                               'longitudinal-rate'):
                if 'count' in field:
                    suffix = 'D'
                elif 'percent' in field or 'rate' in field or 'avg' in field:
                    suffix = 'R'

                if 'four_year_graduate' in field and (
                        short_code == 'S' or short_code == 'R'):
                    code = code[:-1]

                if 'four_year_graduate' in field and 'count' in field:
                    suffix = 'N'

                datum = row[short_code + code + short_year + suffix]
            else:
                datum = row[short_code + code]

            if datum == '.':
                datum = None

            payload[field] = datum

        return payload
