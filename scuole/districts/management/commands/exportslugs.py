# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv

from django.core.management.base import BaseCommand
from scuole.districts.models import *
from scuole.campuses.models import *


class Command(BaseCommand):
    help = "Exporting data"

    def add_arguments(self, parser):
        parser.add_argument('-s', '--shape')

    def handle(self, *args, **options):
        shape = options.get('shape')
        output_dir = 'workspace/a_f_scores/raw_data/'

        shapes_array = ['district', 'campus']

        with open(output_dir + 'campus_district_slugs.csv', 'w+') as csv_file:
                writer = csv.writer(csv_file)

                header_row = ['tea_id', 'absolute_url']
                writer.writerow(header_row)

                print('Creating csv with slugs')

                for shape in shapes_array:
                    if shape == 'district':
                        shapes = District.objects.all()
                    elif shape == 'campus':
                        shapes = Campus.objects.all()

                    for i in shapes:
                        writer.writerow([int(i.tea_id), i.get_absolute_url()])

        print('---')
        print('done')
