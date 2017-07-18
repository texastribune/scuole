# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

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
