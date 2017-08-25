# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db.models import DecimalField, FloatField, IntegerField

from scuole.counties.models import County, CountyCohorts
from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts
from scuole.stats.models import SchoolYear

from slugify import slugify


class Command(BaseCommand):
    help = 'Loads a school year worth of cohorts data.'

    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        if options['year'] is None:
            raise CommandError('A year is required.')

        # get cohorts folder
        cohorts_folder = os.path.join(settings.DATA_FOLDER, 'cohorts')

        # make sure year passed in actually has folder
        self.year_folder = os.path.join(cohorts_folder, options['year'])

        if not os.path.isdir(self.year_folder):
            raise CommandError(
                '`{}` was not found in your cohorts data directory'.format(
                    self.year_folder))

        year = int(options['year'])
        firstYear = year - 1
        secondYear = year

        schoolYear = '{0}-{1}'.format(firstYear, secondYear)

        # if it is there, we get or create our SchoolYear model
        year, _ = SchoolYear.objects.get_or_create(
            name=schoolYear)

        self.year = year

        self.load_regions_state()
        self.load_counties()

    def get_state_model_instance(self):
        return State.objects.get(name='TX')

    def get_region_model_instance(self, identifier, instance):
        return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    def get_county_model_instance(self, identifier, instance):
        return instance.objects.get(fips=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Count not find {}'.format(identifier))
            return None

        return model

    def prep_payload(self, payload, row):
        payload['defaults'].update(self.prepare_row(row))

        payload['ethnicity'] = payload['defaults']['ethnicity']
        payload['gender'] = payload['defaults']['gender']
        payload['economic_status'] = payload['defaults']['economic_status']

    def load_regions_state(self):
        data = []

        data_file = os.path.join(self.year_folder, 'regionState.csv')

        with open(data_file) as f:
            reader = csv.DictReader(f)
            data.append([i for i in reader])

        id_match = 'Region Code'

        for row in sum(data, []):
            if row[id_match] is '' or None:

                payload = {
                    'year': self.year,
                    'defaults': {}
                }
                model = self.get_state_model_instance()
                payload['state'] = model

                self.prep_payload(payload, row)
                StateCohorts.objects.sum_update_or_create(**payload)

                self.stdout.write(model.name)
            else:
                identifier = row[id_match].zfill(2)
                payload = {
                    'year': self.year,
                    'defaults': {}
                }
                model = self.get_region_model_instance(identifier, Region)
                payload['region'] = model

                self.stdout.write(model.name)

                self.prep_payload(payload, row)
                RegionCohorts.objects.update_or_create(**payload)

        self.create_regions_gender_overall()
        self.create_regions_ethnicity_overall()
        self.create_state_ethnicity_overall()

    def load_counties(self):
        counties_fips_id_file = os.path.join(
            settings.DATA_FOLDER, 'cohorts', 'reference',
            'county-fips-id-map.csv')

        county_files = [
            os.path.join(self.year_folder, 'countyEcon.csv'),
            os.path.join(self.year_folder, 'countyGender.csv'),
            os.path.join(self.year_folder, 'countyEthnicity.csv')]

        counties = []
        with open(counties_fips_id_file) as f:
            reader = csv.DictReader(f)
            counties.append([i for i in reader])

        data = []
        for file_name in county_files:
            with open(file_name) as f:
                reader = csv.DictReader(f)
                data.append([i for i in reader])

        for row in sum(data, []):
            if row['County Name'] == '' or ('ethnicity' in row and row['ethnicity'] == 'All ethnicities'):
                continue
            # This is bad and I know it.
            # Loops through the counties in the FIPS/THECB id map sheet
            # and matches it to the FIPS code stored in the County model
            master_name = slugify(row['County Name'])
            for i in sum(counties, []):
                map_name = slugify(i['THECB County Name'])
                if master_name == map_name:
                    identifier = i['FIPS'].zfill(3)

            payload = {
                'year': self.year,
                'defaults': {}
            }

            model = self.get_county_model_instance(identifier, County)
            payload['county'] = model

            self.stdout.write(model.name)

            payload['defaults'].update(self.prepare_row(row))

            payload['economic_status'] = payload['defaults'].get('economic_status', '')
            payload['gender'] = payload['defaults'].get('gender', '')
            payload['ethnicity'] = payload['defaults'].get('ethnicity', '')

            CountyCohorts.objects.sum_update_or_create(**payload)

        self.create_counties_overall()

    def create_counties_overall(self):
        # get the male/female overall cohorts we just created
        new_cohorts = CountyCohorts.objects.filter(
            economic_status='', ethnicity='', year=self.year)

        # get only the counties those cohorts interacted with
        counties = County.objects.filter(cohorts__in=new_cohorts).distinct()

        default_fields = [i.name for i in CountyCohorts._meta.get_fields() if isinstance(i, (
                DecimalField, FloatField, IntegerField,))]

        # loop 'em
        for county in counties:
            # filter new_cohorts for just the two we need
            cohorts_to_combine = new_cohorts.filter(county=county)

            # let's be sure we only have two to work with
            assert len(cohorts_to_combine) == 2, 'There should be only two cohorts'

            for cohort in cohorts_to_combine:
                payload = {
                    'year': self.year,
                    'county': county,
                    'economic_status': '',
                    'ethnicity': '',
                    'gender': '',
                    'defaults': dict((name, getattr(cohort, name)) for name in default_fields),
                }

                CountyCohorts.objects.sum_update_or_create(**payload)

    def create_regions_gender_overall(self):
        # get the ethnicity cohorts we just created
        new_cohorts = RegionCohorts.objects.exclude(ethnicity='').filter(
            economic_status='', year=self.year)

        # get only the regions those cohorts interacted with
        regions = Region.objects.filter(cohorts__in=new_cohorts).distinct()

        default_fields = [i.name for i in RegionCohorts._meta.get_fields() if isinstance(i, (
                DecimalField, FloatField, IntegerField,))]

        # loop 'em
        for region in regions:
            # filter new_cohorts for just the eight we need
            cohorts_to_combine = new_cohorts.filter(region=region)

            # let's be sure we only have eight to work with
            assert len(cohorts_to_combine) == 8, 'There should be only eight cohorts'

            for cohort in cohorts_to_combine:
                payload = {
                    'year': self.year,
                    'region': region,
                    'economic_status': '',
                    'ethnicity': '',
                    'gender': cohort.gender,
                    'defaults': dict((name, getattr(cohort, name)) for name in default_fields),
                }

                RegionCohorts.objects.sum_update_or_create(**payload)

    def create_regions_ethnicity_overall(self):
        # get the gender cohorts we just created
        new_cohorts = RegionCohorts.objects.exclude(ethnicity='').filter(
            economic_status='', year=self.year)

        # get only the regions those cohorts interacted with
        regions = Region.objects.filter(cohorts__in=new_cohorts).distinct()

        default_fields = [i.name for i in RegionCohorts._meta.get_fields() if isinstance(i, (
                DecimalField, FloatField, IntegerField,))]

        # loop 'em
        for region in regions:
            # filter new_cohorts for just the eight we need
            cohorts_to_combine = new_cohorts.filter(region=region)

            # let's be sure we only have eight to work with
            assert len(cohorts_to_combine) == 8, 'There should be only eight cohorts'

            for cohort in cohorts_to_combine:
                payload = {
                    'year': self.year,
                    'region': region,
                    'economic_status': '',
                    'ethnicity': cohort.ethnicity,
                    'gender': '',
                    'defaults': dict((name, getattr(cohort, name)) for name in default_fields),
                }

                RegionCohorts.objects.sum_update_or_create(**payload)

    def create_state_ethnicity_overall(self):
        # get the gender cohorts we just created
        new_cohorts = StateCohorts.objects.exclude(ethnicity='').filter(
            economic_status='', year=self.year)

        # get only the regions those cohorts interacted with
        states = State.objects.filter(cohorts__in=new_cohorts).distinct()
        default_fields = [i.name for i in StateCohorts._meta.get_fields() if isinstance(i, (
                DecimalField, FloatField, IntegerField,))]

        # loop 'em
        for state in states:
            # filter new_cohorts for just the eight we need
            cohorts_to_combine = new_cohorts.filter(state=state)

            # let's be sure we only have eight to work with
            assert len(cohorts_to_combine) == 8, 'There should be only eight cohorts'

            for cohort in cohorts_to_combine:
                payload = {
                    'year': self.year,
                    'state': state,
                    'economic_status': '',
                    'ethnicity': cohort.ethnicity,
                    'gender': '',
                    'defaults': dict((name, getattr(cohort, name)) for name in default_fields),
                }

                StateCohorts.objects.sum_update_or_create(**payload)

    def prepare_row(self, row):
        fields = [
            'enrolled_8th',
            'enrolled_9th',
            'enrolled_10th',
            'lessthan_10th_enrolled',
            'graduated',
            'enrolled_4yr',
            'enrolled_2yr',
            'enrolled_out_of_state',
            'total_enrolled',
            'enrolled_wo_record',
            'total_degrees',
            'ethnicity',
            'gender',
            'economic_status'
        ]

        problem_children = ['', '-', '.', '#VALUE!']
        pivots = ['ethnicity', 'gender', 'economic_status']
        payload = {}
        ethnicities = ['White', 'African American', 'Hispanic', 'Others', 'All Ethnicities', '']

        for field in row:
            if field in fields:
                datum = row[field]
                # If the data's masked or blank, return blanks for the pivots
                # that are strings or nulls for everything else
                if datum.strip() in problem_children:
                    if field in pivots:
                        datum = ''
                    else:
                        datum = None
                # otherwise return the data
                else:
                    datum = row[field]

                # if the ethnicity is anything other than white, Hispanic,
                # black or others, change the ethnicity to 'others' and sum
                # it with the rest of the others for consistency across years
                if field == 'ethnicity':
                    if datum not in ethnicities:
                        datum = 'Others'

                payload[field] = datum

        return payload
