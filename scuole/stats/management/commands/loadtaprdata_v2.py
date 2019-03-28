from csv import DictReader
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
    "reference.csv",
    "longitudinal-rate.csv",
    "postsecondary-readiness-and-non-staar-performance-indicators.csv",
    "staff-and-student-information.csv",
    "attendance.csv",
)

AF_ACCOUNTABILITY_FIELDS = (
    "student_achievement_rating",
    "school_progress_rating",
    "closing_the_gaps_rating",
)

ACCOUNTABILITY_FIELDS = ("accountability_rating",) + AF_ACCOUNTABILITY_FIELDS


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

        for mapping in MAPPING:
            name = mapping.get("folder")
            id_column = mapping.get("identifier")
            id_field = mapping.get("id_field")
            active_model = mapping.get("model")
            short_code = mapping.get("short_code")
            stats_model = mapping.get("stats_model")

            raw_data = []

            try:
                stats_model._meta.get_field("accountability_rating")
                include_accountability_rating = True
            except FieldDoesNotExist:
                include_accountability_rating = False

            for file_name in DATA_FILES:
                if file_name == "reference.csv" and not include_accountability_rating:
                    continue

                data_file_path = path.join(data_folder, name, file_name)

                # if the file doesn't exist just move on, it'll crash elsewhere if it matters
                if not path.isfile(data_file_path):
                    continue

                with open(data_file_path) as f:
                    reader = DictReader(f)
                    raw_data.append([i for i in reader])

            data = self.data_list_joiner(id_column, raw_data)

            bulk_list = []

            for row in data:
                identifier = row.get(id_column)

                instance = self.get_model_instance(
                    name, identifier, id_field, active_model
                )

                self.stdout.write(instance.name)

                try:
                    stats_model._meta.get_field("accountability_rating")
                    include_accountability_rating = True
                except FieldDoesNotExist:
                    include_accountability_rating = False

                payload = {"year": school_year, "defaults": {}, name: instance}

                for field_name, template in SCHEMA.items():
                    # skip the accountability fields for things that don't have those (state and region)
                    if (
                        field_name in ACCOUNTABILITY_FIELDS
                        and not include_accountability_rating
                    ):
                        continue

                    # skip the AF accountability fields for campuses, 2017-2018 is the transition year
                    if (
                        field_name in AF_ACCOUNTABILITY_FIELDS
                        and name == "campus"
                        and year == "2017-2018"
                    ):
                        continue

                    if "four_year_graduate" in field_name and short_code in ("C", "D"):
                        suffix = "X"
                    else:
                        suffix = ""

                    column = template.format(
                        short_code=short_code, year=short_year, suffix=suffix
                    )
                    value = row[column]

                    if value == ".":
                        value = None

                    payload["defaults"][field_name] = value

                # The A-F transition made campus accountability weird
                if year == "2017-2018" and include_accountability_rating:
                    for field in ACCOUNTABILITY_FIELDS:
                        if field not in payload["defaults"]:
                            continue

                        payload["defaults"][field] = stats_model.RATING_MATCH_17_18.get(
                            payload["defaults"][field], payload["defaults"][field]
                        )

                # We have to flag whether we're in A-F land or not
                if "student_achievement_rating" in payload["defaults"]:
                    payload["defaults"]["uses_legacy_ratings"] = False

                if use_bulk:
                    bulk_payload = payload["defaults"]
                    bulk_payload["year"] = payload["year"]
                    bulk_payload[name] = payload[name]

                    bulk_list.append(stats_model(**bulk_payload))
                else:
                    stats_model.objects.update_or_create(**payload)

            if use_bulk:
                stats_model.objects.bulk_create(bulk_list)

    def data_list_joiner(self, key, data):
        output = {}

        if key:
            all_data = sum(data, [])

            for item in all_data:
                if item[key] in output:
                    output[item[key]].update(item)
                else:
                    output[item[key]] = item
        else:
            output["STATE"] = {}

            for d in data:
                output["STATE"].update(d[0])

        return [i for (_, i) in output.items()]

    def get_model_instance(self, name, identifier, id_field, Model):
        if name == "state":
            return State.objects.get(name="TX")

        try:
            model = Model.objects.get(**{id_field: identifier})
        except Model.DoesNotExist:
            self.stderr.write("Could not find {}".format(identifier))
            return None

        return model
