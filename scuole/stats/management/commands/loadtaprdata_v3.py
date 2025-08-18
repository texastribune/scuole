# LOADTAPRDATA_V3
# 3/3/25
# RR loadtaprdata_v2 didn't work out of the box for my first data import (SY2022-23), so I'm tailoring it here, preserving the old v2 as a separate file
# rebranded vague "name" to jurisdiction

from csv import DictReader
from collections import defaultdict
from os import path

from django.conf import settings
from django.core.exceptions import FieldDoesNotExist
from django.core.management.base import BaseCommand, CommandError

from scuole.stats.schemas.tapr.mapping import MAPPING
from scuole.stats.schemas.tapr.schema_v2 import SCHEMA
from scuole.stats.models import SchoolYear
from scuole.states.models import State

DATA_FILES = (
    "accountability.csv",
    "accountability_2018-2019.csv",
    "reference.csv",
    "longitudinal-rate.csv",
    "postsecondary-readiness-and-non-staar-performance-indicators.csv",
    "ap-ib-sat-act.csv",
    "staff-and-student-information.csv",
    "attendance.csv",
    #"testing.csv",
)

AF_ACCOUNTABILITY_FIELDS = (
    "student_achievement_rating",
    "school_progress_rating",
    "closing_the_gaps_rating",
    "student_achievement_rating_18_19",
    "school_progress_rating_18_19",
    "closing_the_gaps_rating_18_19",
)

ACCOUNTABILITY_FIELDS = ("accountability_rating","accountability_rating_18_19") + AF_ACCOUNTABILITY_FIELDS

# 8/18/25 RR hardcoding to pull newer accountability data, instead of older data from TAPR dataset
ACCOUNTABILITY_YEAR_OVERRIDE = "2024-2025"

class Command(BaseCommand):
    help = "Loads a school year's worth of TAPR data."

    def add_arguments(self, parser):
        parser.add_argument("year")
        parser.add_argument("--bulk", action="store_true")

    def handle(self, *args, **options):
        year = options.get("year")
        use_bulk = options.get("bulk")

        data_folder = path.join(settings.DATA_FOLDER, "tapr", year)

        if not path.isdir(data_folder):
            raise CommandError(
                "`{}` was not found in your TAPR data directory".format(data_folder)
            )

        # if it is there, we get or create the SchoolYear model
        school_year, _ = SchoolYear.objects.get_or_create(name=year)
        short_year = school_year.name.split("-")[0][2:]

        # mapping is divided into 4 units: state, region, district, campus
        for mapping in MAPPING:
            # these properties help us identify data columns for each unit's data files
            # i.e. all of a district's data columns start with 'D'
            jurisdiction = mapping.get("folder")
            self.stdout.write(f"--------------------\nLoading {jurisdiction} TAPR data for {year}\n--------------------")
            id_column = mapping.get("identifier")
            id_field = mapping.get("id_field")
            active_model = mapping.get("model")
            short_code = mapping.get("short_code")
            stats_model = mapping.get("stats_model")
            prepared_schema = {}

            # add a suffix for some columns in the schema
            for field_name, template in SCHEMA.items():
                if "four_year_graduate" in field_name and short_code in ("C", "D"):
                    suffix = "X"
                else:
                    suffix = ""

                column = template.format(
                    short_code=short_code, year=short_year, suffix=suffix
                )

                # map the meaning of each file's column to the column name
                # i.e. 'african_american_count': "DPETBLAC"
                prepared_schema[field_name] = column

            # check if the corresponding model has an A-F rating field (campuses and districts should have this)
            # tempoerarily removed accountability ratings for SY2022-23 and beyond (3/3/25 RR, to 8/18/25)
            # self.stdout.write(self.style.ERROR("ignoring accountability rating (for SY2022-23 and beyond)"))
            include_accountability_rating = False
            try:
                stats_model._meta.get_field("accountability_rating")
                include_accountability_rating = True
            except FieldDoesNotExist:
                include_accountability_rating = False

            self.matched_data = defaultdict(dict)

            # loop through each file for each unit
            for file_name in DATA_FILES:
                # 8/18/25 accountability data override, if I want newer A-F ratings than were published with TAPR
                current_data_folder_for_file = data_folder

                if file_name == "accountability.csv" and ACCOUNTABILITY_YEAR_OVERRIDE:
                    base_dir_before_year = path.dirname(data_folder)
                    
                    # Construct the new data folder path using the override year
                    current_data_folder_for_file = path.join(base_dir_before_year, ACCOUNTABILITY_YEAR_OVERRIDE)
                    self.stdout.write(f"Override: Using year '{ACCOUNTABILITY_YEAR_OVERRIDE}' for '{file_name}'. Effective path base: {current_data_folder_for_file}")

                self.stdout.write(f"loading {file_name} from effective folder: {current_data_folder_for_file}/{jurisdiction}")

                # Original logic for skipping reference.csv if not including accountability rating
                if file_name == "reference.csv" and not include_accountability_rating:
                    self.stdout.write(f"skipping reference for non-accountability files")
                    continue

                data_file_path = path.join(current_data_folder_for_file, jurisdiction, file_name)

                # if the file doesn't exist just move on, it'll crash elsewhere if it matters
                if not path.isfile(data_file_path):
                    self.stdout.write(self.style.ERROR(f"{file_name} not found"))
                    continue

                with open(data_file_path) as f:
                    reader = DictReader(f)

                    # data_list_joiner filters out any not matching columns
                    self.data_list_joiner(id_column, reader, prepared_schema.values(), file_name)

                if mapping.get("folder") == 'district' and file_name == 'accountability.csv':
                    print(prepared_schema.values())
                    print(data)
                    print(self.matched_data.values())

            # get the columns from the data that are included in the prepared_schema
            data = self.matched_data.values()
            # 3/3/25 to 8/17/25 commented this out b/c no ratings for SY2022-23 and beyond
            if mapping['folder'] == 'district' or mapping['folder'] == 'campus':
                data = [x for x in data if f'{short_code}_RATING' in x]

            self.stdout.write(f"Count of entities to process: {len(data)}")
            if len(data) == 0:
                self.stdout.write(self.style.WARNING("No data matches your filter criteria"))
                # You could also print what's in self.matched_data to see what you have
                self.stdout.write(f"Five keys in matched_data: {list(self.matched_data.keys())[:5]}")  # Show first 5 keys
                # If you need more detail, you could dump a sample
                if self.matched_data:
                    sample_key = next(iter(self.matched_data))
                    self.stdout.write(f"Sample data: {self.matched_data[sample_key]}")

            bulk_list = []

            # loop through the formatted data
            for row in data:
                # get the identifier, AKA the TEA ID of the district or campus
                # i.e. for districts, the identifier is 'DISTRICT'
                identifier = row.get(id_column)

                # get the model instance with the identifier
                instance = self.get_model_instance(
                    jurisdiction, identifier, id_field, active_model
                )

                # write the instance name out to the terminal so we know
                # self.stdout.write(instance.name)
                try:
                    self.stdout.write(f"processing {jurisdiction} ({identifier}): {instance.name}")
                except AttributeError:
                    print(f"\033[91mWarning: Could not find name for instance ID {identifier}\033[0m")
                    continue
                
                # instance = self.get_model_instance(
                #     name, identifier, id_field, active_model
                # )

                # # write the instance name out to the terminal so we know
                # # self.stdout.write(instance.name)
                # try:
                #     self.stdout.write(instance.name)
                # except AttributeError:
                #     print(f"\033[91mWarning: Could not find name for instance ID {instance_id}\033[0m")
                #     continue
                
                # check if the corresponding model has an A-F rating field
                include_accountability_rating = False
                try:
                    stats_model._meta.get_field("accountability_rating")
                    include_accountability_rating = True
                except FieldDoesNotExist:
                    include_accountability_rating = False

                payload = {"year": school_year, "defaults": {}, jurisdiction: instance}

                # loop through the schema again
                for field_name, template in SCHEMA.items():
                    # skip the accountability fields for things that don't have those (state and region)
                    if (
                        field_name in ACCOUNTABILITY_FIELDS
                        and not include_accountability_rating
                    ):
                        continue

                    if "four_year_graduate" in field_name and short_code in ("C", "D"):
                        suffix = "X"
                    else:
                        suffix = ""

                    column = template.format(
                        short_code=short_code, year=short_year, suffix=suffix
                    )

                    if column not in row:
                        if column in [f'{short_code}D1G', f'{short_code}D2G', f'{short_code}D3G']:
                            value = row[f'{short_code}_RATING']
                        else:
                            value = None
                    else:
                        value = row[column]

                    if value == ".":
                        value = None

                    payload["defaults"][field_name] = value

                # We have to flag whether we're in A-F land or not
                if "student_achievement_rating" in payload["defaults"]:
                    payload["defaults"]["uses_legacy_ratings"] = False

                if include_accountability_rating:
                    # In 2018-2019, some accountability ratings showed up as 'Data Integrity Issues', which is 
                    # not a choice in `reference.py`, so we replace it with `Q` which we do list and is
                    # the code for that problem
                    if payload['defaults']['accountability_rating'] == 'Data Integrity Issues':
                        payload['defaults']['accountability_rating'] = 'Q'
                    if payload['defaults']['accountability_rating_18_19'] == 'Data Integrity Issues':
                        payload['defaults']['accountability_rating_18_19'] = 'Q'

                    for field in ACCOUNTABILITY_FIELDS:
                        if field not in payload["defaults"]:
                            continue
                        
                        # Ratings may not show up as a code (i.e. "Not Rated")
                        # so we match the rating up to a code with RATING_MATCH
                        # in `reference.py`
                        if payload["defaults"]["uses_legacy_ratings"] == False:
                          payload["defaults"][field] = stats_model.RATING_MATCH.get(
                            payload["defaults"][field], payload["defaults"][field]
                        )
                        
                        else:
                            payload["defaults"][field] = stats_model.RATING_MATCH_LEGACY.get(
                            payload["defaults"][field], payload["defaults"][field]
                        )
                            

                if use_bulk:
                    bulk_payload = payload["defaults"]
                    bulk_payload["year"] = payload["year"]
                    bulk_payload[jurisdiction] = payload[jurisdiction]

                    bulk_list.append(stats_model(**bulk_payload))
                else:
                    stats_model.objects.update_or_create(**payload)

            if use_bulk:
                stats_model.objects.bulk_create(bulk_list)

    def data_list_joiner(self, id_column, data, valid_keys, file_name):
        # loop through each row in the data
        for item in data:
            # get the unique ID
            uid = item.get(id_column, "STATE")

            # filter out non-matching keys
            clean_item = {key: item[key] for key in valid_keys if key in item}

            # include the unique ID
            clean_item[id_column] = uid

            # update the matcher
            self.matched_data[uid].update(clean_item)

    def get_model_instance(self, name, identifier, id_field, Model):
        if name == "state":
            return State.objects.get(name="TX")

        # to see every model object
        # print(Model.objects.all())

        if name == 'district' and id_field == 'tea_id':
            identifier = str(identifier).zfill(6)

        if name == 'campus' and id_field == 'tea_id':
            identifier = str(identifier).zfill(9)

        try:
            model = Model.objects.get(**{id_field: identifier})
        except Model.DoesNotExist:
            self.stderr.write("Could not find {}".format(identifier))
            return None

        return model
