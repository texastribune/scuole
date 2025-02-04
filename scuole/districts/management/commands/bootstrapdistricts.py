# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import json
import os

from django.conf import settings
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count

from slugify import slugify

from scuole.core.replacements import ISD_REPLACEMENT
from scuole.core.utils import massage_name, remove_charter_c
from scuole.counties.models import County
from scuole.regions.models import Region

from ...models import District


class Command(BaseCommand):
    help = "Bootstraps District models using TEA, FAST and AskTED data."

    def add_arguments(self, parser):
        parser.add_argument("year", nargs="?", type=str, default=None)

    def handle(self, *args, **options):
        if options["year"] is None:
            raise CommandError("A year is required.")

        fast_file_location = os.path.join(
            settings.DATA_FOLDER, "fast", "fast-district.csv"
        )

        self.fast_data = self.load_fast_file(fast_file_location)

        district_json = os.path.join(
            settings.DATA_FOLDER,
            "tapr",
            "reference",
            "district",
            "shapes",
            "districts.geojson",
        )

        self.shape_data = self.load_geojson_file(district_json)

        superintendent_csv = os.path.join(
            settings.DATA_FOLDER, "askted", "district", "superintendents.csv"
        )

        # path to file where new, cleaned up district names and IDs are stored
        new_districts = os.path.join(
            settings.DATA_FOLDER,
            "tapr",
            "reference",
            "district",
            "updates",
            options["year"],
            "new_districts.csv",
        )

        self.newDistrict_data = self.load_newDistrict_file(new_districts)

        # path to file where new, cleaned up names and IDs of districts whose
        # names have changed since the last update
        changed_districts = os.path.join(
            settings.DATA_FOLDER,
            "tapr",
            "reference",
            "district",
            "updates",
            options["year"],
            "changed_districts.csv",
        )

        self.changedDistrict_data = self.load_changedDistrict_file(changed_districts)

        self.superintendent_data = self.load_superintendent_file(superintendent_csv)

        tea_file = os.path.join(
            settings.DATA_FOLDER,
            "tapr",
            "reference",
            "district",
            "reference",
            "reference.csv",
        )

        with open(tea_file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                self.create_district(row)

        self.make_slugs_unique()

    def load_fast_file(self, file):
        payload = {}

        with open(file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                payload[row["District Number"]] = row

        return payload

    def load_geojson_file(self, file):
        payload = {}

        with open(file, "r") as f:
            data = json.load(f)

            for feature in data["features"]:
                tea_id = feature["properties"]["DISTRICT_C"]
                payload[tea_id] = feature["geometry"]

        return payload

    def load_superintendent_file(self, file):
        payload = {}

        with open(file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row["District Number"].replace("'", "")
                payload[tea_id] = row

        return payload

    def load_newDistrict_file(self, file):
        payload = {}

        with open(file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row["District Number"]
                payload[tea_id] = row

        return payload

    def load_changedDistrict_file(self, file):
        payload = {}

        with open(file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row["District Number"]
                payload[tea_id] = row

        return payload

    def create_district(self, district):
        district_id = str(int(district["DISTRICT"]))

        # first checks to see if the District ID is in both the changed
        # district data and FAST data
        if district_id in self.changedDistrict_data and self.fast_data:
            # if it is, it'll update the existing name to the new name
            # in the changed district CSV
            fast_match = self.changedDistrict_data[district_id]
        # then it'll look to see if the ID is in the FAST data
        elif district_id in self.fast_data:
            # if it is, it'll use the nice name in there
            fast_match = self.fast_data[district_id]
        # if the ID isn't in the changed list or in the FAST data, it'll
        # check if it's in the new district list
        elif district_id in self.newDistrict_data:
            # if it is, it'll use the name in the new district data
            fast_match = self.newDistrict_data[district_id]
        # if there are no clean name options anywhere, we'll use our name
        # massager and clean it up there
        else:
            fast_match = {
                "District Name": massage_name(district["DISTNAME"], ISD_REPLACEMENT)
            }

        name = remove_charter_c(fast_match["District Name"])
        self.stdout.write("Creating {}...".format(name))
        county = County.objects.get(name__iexact=district["CNTYNAME"])
        region = Region.objects.get(region_id=district["REGION"])

        if district["DFLCHART"] == "N":
            charter = False
        else:
            charter = True

        if district["DISTRICT"] in self.shape_data:
            geometry = GEOSGeometry(json.dumps(self.shape_data[district["DISTRICT"]]))

            # checks to see if the geometry is a multipolygon
            if geometry.geom_typeid == 3:
                geometry = MultiPolygon(geometry)
        else:
            self.stderr.write("No shape data for {}".format(name))
            geometry = None

        instance, _ = District.objects.update_or_create(
            tea_id=district["DISTRICT"],
            defaults={
                "name": name,
                "slug": slugify(name),
                "charter": charter,
                "region": region,
                "county": county,
                "shape": geometry,
            },
        )

    def make_slugs_unique(self):
        models = (
            District.objects.values("slug")
            .annotate(Count("slug"))
            .order_by()
            .filter(slug__count__gt=1)
        )
        slugs = [i["slug"] for i in models]

        districts = District.objects.filter(slug__in=slugs)

        for district in districts:
            district.slug = "{0}-{1}".format(district.slug, district.county.slug)
            district.save()
