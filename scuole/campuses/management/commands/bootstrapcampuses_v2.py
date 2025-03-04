from csv import DictReader
from json import dumps, load
from os.path import join

from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from scuole.campuses.models import Campus
from scuole.counties.models import County
from scuole.districts.models import District


class Command(BaseCommand):
    help = "Bootstraps Campus models using TEA, FAST and AskTED data."

    def add_arguments(self, parser):
        parser.add_argument("year", nargs="?", type=str, default=None)

    def handle(self, *args, **options):
        self.year = options.get("year")

        if not self.year:
            raise CommandError("A year is required.")

        entities_file = join(
            settings.DATA_FOLDER, f"tapr/{self.year}/campus/entities.csv"
        )

        with open(entities_file) as infile:
            campuses = [row for row in DictReader(infile)]

        campuses_geojson_file = join(
            settings.DATA_FOLDER, "tapr/reference/campus/shapes/campuses.geojson"
        )

        shape_data = {}

        with open(campuses_geojson_file) as infile:
            geo_data = load(infile)
            features = geo_data.get("features")

            for feature in features:
                properties = feature.get("properties")

                #raw_id = str(int(properties.get("School_Num").replace("'", '')))
                raw_id = properties.get("USER_School_Number")
                if raw_id:
                    raw_id = str(int(raw_id.replace("'", '')))
                else:
                    #print(f"\033[31mWarning: Missing School_Num for properties: {properties}\033[0m")
                    print(f"\033[31mWarning: Missing School_Num for USER_District_Name: {properties.get('USER_District_Name')}\033[0m")
                    continue
                tea_id = raw_id

                # a campus ID is typically 9 digits
                # in the new geoJSON data, the campus ID's are formatted weirdly
                if (len(raw_id) < 9):
                    tea_id = ((9 - len(raw_id)) * '0') + raw_id

                shape_data[tea_id] = feature.get("geometry")

        self.shape_data = shape_data

        for campus in campuses:
            self.create_campus(campus)

    def create_campus(self, data):
        campus_id = str(data.get("CAMPUS")).zfill(9)
        campus_name = data.get("CAMPNAME_CLEAN")
        county_state_code = data.get("COUNTY").zfill(3)
        district_id = str(data.get("DISTRICT")).zfill(6)

        school_type = data["GRDTYPE"]
        low_grade, high_grade = data["GRDSPAN"].split(" - ")
        is_charter = data["CFLCHART"] == "Y"

        district = District.objects.get(tea_id=district_id)
        county = County.objects.get(state_code=county_state_code)

        self.stdout.write(f"Creating {campus_name} in ({campus_id})")

        geometry_data = self.shape_data.get(campus_id)
        if geometry_data:
            geometry = GEOSGeometry(dumps(geometry_data))
        else:
            geometry = None
            self.stderr.write(f"No shape data for {campus_name}")

        # if campus_id in self.shape_data:
        #     geometry = GEOSGeometry(dumps(self.shape_data.get(campus_id)))
        # else:
        #     geometry = None
        #     self.stderr.write(f"No shape data for {campus_name}")

        instance, _ = Campus.objects.update_or_create(
            tea_id=campus_id,
            defaults={
                "name": campus_name,
                "slug": slugify(campus_name, allow_unicode=True),
                "charter": is_charter,
                "coordinates": geometry,
                "low_grade": low_grade,
                "high_grade": high_grade,
                "school_type": school_type,
                "district": district,
                "county": county,
            },
        )
