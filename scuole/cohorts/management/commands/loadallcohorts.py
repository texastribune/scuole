# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db.models import DecimalField, FloatField, IntegerField

from slugify import slugify

from scuole.counties.models import County, CountyCohorts
from scuole.regions.models import Region, RegionCohorts
from scuole.states.models import State, StateCohorts
from scuole.stats.models import SchoolYear

class Command(BaseCommand):
    help = 'Loads a school year worth of cohorts data.'

    # only loads data for the year you give it
    def add_arguments(self, parser):
        parser.add_argument('year', nargs='?', type=str, default=None)

    # if there's no year, it yells at you
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
        # creates the school year based on the given year
        schoolYear = '{0}-{1}'.format(firstYear, secondYear)

        # if it is there, we get or create our SchoolYear model
        year, _ = SchoolYear.objects.get_or_create(
            name=schoolYear)

        self.year = year

        # loads the region/state combo file and all county data
        self.load_regions_state()
        self.load_counties()

    def get_state_model_instance(self):
        return State.objects.get(name='TX')

    # gets the region model that corresponds to the data we're handling
    def get_region_model_instance(self, identifier, instance):
        return instance.objects.get(region_id=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Could not find {}'.format(identifier))
            return None

        return model

    # gets the county model that corresponds to the data we're handling
    def get_county_model_instance(self, identifier, instance):
        return instance.objects.get(fips=identifier)

        try:
            model = instance.objects.get(cohorts=identifier)
        except instance.DoesNotExist:
            self.stderr.write('Count not find {}'.format(identifier))
            return None

        return model

    # preps the data to load into the model
    def prep_payload(self, payload, row):
        payload['defaults'].update(self.prepare_row(row))

        payload['ethnicity'] = payload['defaults']['ethnicity']
        payload['gender'] = payload['defaults']['gender']
        payload['economic_status'] = payload['defaults']['economic_status']

    # loads the region/state combo file
    def load_regions_state(self):
        data = []

        data_file = os.path.join(self.year_folder, 'regionState.csv')

        # opens the data file and adds the data from each row to the data list
        with open(data_file, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            data.append([i for i in reader])

        id_match = 'Region Code'

        for row in sum(data, []):
            # if it's a row where 'Region Code' is blank, it's state data
            if row[id_match] == '' or None:
                # sets up the payload
                payload = {
                    'year': self.year,
                    'defaults': {}
                }

                # grabs the state model (we only have one state, TX)
                model = self.get_state_model_instance()
                payload['state'] = model

                # preps the data and updates or creates a state cohort model
                self.prep_payload(payload, row)
                StateCohorts.objects.sum_update_or_create(**payload)

                self.stdout.write(model.name)
            else:
                # tells us which region we're talking about. TEA's regions
                # are zero indexed, THECB's are not
                identifier = row[id_match].zfill(2)
                payload = {
                    'year': self.year,
                    'defaults': {}
                }
                # gets the model based on whatever the region number is
                model = self.get_region_model_instance(identifier, Region)
                payload['region'] = model

                self.stdout.write(model.name)

                self.prep_payload(payload, row)

                # creates a cohort model for each region
                RegionCohorts.objects.update_or_create(**payload)

        # for both region and state, sort and load the data
        self.create_regions_gender_overall()
        self.create_regions_ethnicity_overall()
        self.create_state_ethnicity_overall()

    # because the counties have 3 different files and not all-in-one, we do
    # them separately
    def load_counties(self):
        # grabs geo data for the counties
        counties_fips_id_file = os.path.join(
            settings.DATA_FOLDER, 'cohorts', 'reference',
            'county-fips-id-map.csv')
        # grabs cohort data for the counties
        county_files = [
            os.path.join(self.year_folder, 'countyEcon.csv'),
            os.path.join(self.year_folder, 'countyGender.csv'),
            os.path.join(self.year_folder, 'countyEthnicity.csv')]

        counties = []
        # grab the data in each row in the fips file
        with open(counties_fips_id_file) as f:
            reader = csv.DictReader(f)
            counties.append([i for i in reader])

        data = []
        # grab the data in all of the county files
        for file_name in county_files:
            with open(file_name) as f:
                reader = csv.DictReader(f)
                data.append([i for i in reader])

        # Skip over the problem children
        for row in sum(data, []):
            if row['County Name'] in ['', 'BRISCOE'] or ('ethnicity' in row and row['ethnicity'] == 'All ethnicities'):
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
            # gets the county based on the identifier
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
        # We sum male/female cohorts as a proxy for total numbers
        new_cohorts = CountyCohorts.objects.filter(
            economic_status='', ethnicity='', year=self.year)

        # get only the counties those cohorts interacted with
        counties = County.objects.filter(cohorts__in=new_cohorts).distinct()

        # grabs the data fields (those for numbers)
        default_fields = [i.name for i in CountyCohorts._meta.get_fields() if isinstance(i, (
                DecimalField, FloatField, IntegerField,))]

        # loop 'em
        for county in counties:
            # filter new_cohorts for just the two we need
            cohorts_to_combine = new_cohorts.filter(county=county)

            # let's be sure we only have two to work with (male/female)
            assert len(cohorts_to_combine) == 2, 'There should be only two cohorts'

            # creates the data for the model, all pivots are blank because
            # these are totals
            for cohort in cohorts_to_combine:
                payload = {
                    'year': self.year,
                    'county': county,
                    'economic_status': '',
                    'ethnicity': '',
                    'gender': '',
                    'defaults': dict((name, getattr(cohort, name)) for name in default_fields),
                }
                # loads the data to the model
                CountyCohorts.objects.sum_update_or_create(**payload)

    def create_regions_gender_overall(self):
        # THECB doesn't give us just region genders like counties, so we
        # have to extrapolate gender totals from gender/ethnicity combo rows
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

            # loop through the eight gender/ethnicity breakdown cohorts for each region
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
        # THECB also doesn't give us just ethnicity data, so we extrapolate
        # from gender/ethnicity combo rows
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
