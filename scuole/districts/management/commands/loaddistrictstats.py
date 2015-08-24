# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from scuole.stats.models import SchoolYear
from ...models import District, DistrictStats


class Command(BaseCommand):
    help = 'Loads TEA district statistics.'

    def handle(self, *args, **options):
        self.school_year, _ = SchoolYear.objects.get_or_create(
            name='2013-2014')

        file_location = os.path.join(
            settings.DATA_FOLDER, 'tapr', '2013-2014',
            'district', 'staff-and-student-information.csv')

        self.data = self.load_file(file_location)

        for entry in self.data:
            self.create_stats(entry)

    def load_file(self, file):
        with open(file) as f:
            return [i for i in csv.DictReader(f)]

    def create_stats(self, data):
        district = District.objects.get(tea_id=data['DISTRICT'])
        self.stdout.write('Loading stats for {}'.format(district.name))

        DistrictStats.objects.get_or_create(
            year=self.school_year,
            district=district,
            all_students_count=int(data['DPETALLC']),
            african_american_count=int(data['DPETBLAC']),
            asian_count=int(data['DPETASIC']),
            hispanic_count=int(data['DPETHISC']),
            pacific_islander_count=int(data['DPETPCIC']),
            two_or_more_races_count=int(data['DPETTWOC']),
            white_count=int(data['DPETWHIC']),
        )
