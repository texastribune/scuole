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
        # parser.add_argument(
        #     '-y',
        #     '--year',
        #     action='store',
        #     dest='year',
        #     default=False,
        #     help='The school year to load (E.g. 2013-2014)')

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

        self.load_staff_students()

    def load_staff_students(self):
        file_name = 'staff-and-student-information.csv'
        schema = SCHEMA[file_name.split('.')[0]]

        missing = []

        for m in MAPPING:
            folder = m['folder']
            current_model = m['model']
            identifier = m['identifier']

            data_file = os.path.join(self.year_folder, folder, file_name)

            with open(data_file) as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if folder == 'state':
                        instance = State.objects.get(name='TX')
                    elif folder == 'region':
                        instance = current_model.objects.get(
                            region_id=row[identifier])
                    else:
                        try:
                            instance = current_model.objects.get(
                                tea_id=row[identifier])
                        except current_model.DoesNotExist:
                            self.stderr.write('Could not find {}'.format(
                                row[identifier]))
                            missing.append(
                                '{}: {}'.format(folder, row[identifier]))
                            continue

                    self.stdout.write(instance.name)

                    payload = {
                        'defaults': {}
                    }

                    payload['year'] = self.school_year
                    payload[folder] = instance

                    for field, code in schema.items():
                        datum = row[m['short_code'] + code]

                        if datum == '.':
                            datum = None

                        payload['defaults'][field] = datum

                    m['stats_model'].objects.update_or_create(**payload)

        if missing:
            self.stderr.write('The following entities were missing: ')
            [self.stderr.write(m) for m in missing]
