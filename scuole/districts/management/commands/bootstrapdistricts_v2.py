from csv import DictReader
from json import dumps, load
from os.path import join

from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from scuole.counties.models import County
from scuole.districts.models import District
from scuole.regions.models import Region


class Command(BaseCommand):
    help = "Bootstraps District models using TEA data."

    def add_arguments(self, parser):
        parser.add_argument("year", nargs="?", type=str, default=None)

    def handle(self, *args, **options):
        self.year = options.get("year")

        if not self.year:
            raise CommandError("A year is required.")

        entities_file = join(
            settings.DATA_FOLDER, f"tapr/{self.year}/district/entities.csv"
        )

        with open(entities_file) as infile:
            districts = [row for row in DictReader(infile)]

        districts_geojson_file = join(
            settings.DATA_FOLDER, "tapr/reference/district/shapes/districts.geojson"
        )

        shape_data = {}

        with open(districts_geojson_file) as infile:
            geo_data = load(infile)
            features = geo_data.get("features")

            for feature in features:
                properties = feature.get("properties")
                tea_id = properties.get("DISTRICT_C")

                shape_data[tea_id] = feature.get("geometry")

        self.shape_data = shape_data

        for district in districts:
            self.create_district(district)

    def create_district(self, data):
        district_id = str(data.get("DISTRICT")).zfill(6)
        district_name = data.get("DISTNAME_CLEAN")
        county_state_code = data.get("COUNTY").zfill(3)
        region_id = str(data.get("REGION")).zfill(2)

        self.stdout.write(f"Creating {district_name} ({district_id})")

        county = County.objects.get(state_code=county_state_code)
        region = Region.objects.get(region_id=region_id)

        is_charter = data["DFLCHART"] == "Y"

        if district_id in self.shape_data:
            geometry = GEOSGeometry(dumps(self.shape_data.get(district_id)))

            # checks to see if the geometry is a MultiPolygon
            if geometry.geom_typeid == 3:
                geometry = MultiPolygon(geometry)
        else:
            geometry = None
            self.stderr.write(f"No shape data for {district_name}")

        instance, _ = District.objects.update_or_create(
            tea_id=district_id,
            defaults={
                "name": district_name,
                "slug": slugify(district_name, allow_unicode=True),
                "charter": is_charter,
                "region": region,
                "county": county,
                "shape": geometry,
            },
        )

