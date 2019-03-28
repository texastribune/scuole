from csv import DictReader

import requests

from django.core.management.base import BaseCommand

from scuole.core.constants import ASKTED_DIRECTORY_URL, ASKTED_DIRECTORY_VIEWSTATE
from scuole.districts.models import District


class Command(BaseCommand):
    help = "Update District models with AskTED data."

    def handle(self, *args, **options):
        # track the ones we've seen so far so we don't waste time
        self.processed_districts = set()

        req = requests.post(
            ASKTED_DIRECTORY_URL,
            data={
                "__VIEWSTATE": ASKTED_DIRECTORY_VIEWSTATE,
                "ddlSortOrder": "School Number",
                "btnDownloadFile": "Download File",
            },
        )

        directory_data = DictReader(req.text.splitlines())

        for row in directory_data:
            self.update_district(row)

    def update_district(self, data):
        # AskTED districts have apostrophes in them, strangely
        district_id = data.get("District Number").replace("'", "").zfill(6)

        if district_id in self.processed_districts:
            return

        self.processed_districts.add(district_id)

        try:
            district = District.objects.get(tea_id=district_id)
        except District.DoesNotExist:
            # if there's no match don't worry about it
            return

        self.stdout.write(f"Updating AskTED data for {district.name} ({district_id})")

        phone_number = data.get("District Phone")
        fax_number = data.get("District Fax")

        # sometimes phone and fax numbers have extensions at the end
        # this splits out the extension into its own field
        if "ext" in phone_number:
            phone_number, phone_number_extension = phone_number.split(" ext:")
        else:
            phone_number_extension = ""

        if "ext" in fax_number:
            fax_number, fax_number_extension = fax_number.split(" ext:")
        else:
            fax_number_extension = ""

        street = data.get("District Street Address")
        city = data.get("District City")
        state = data.get("District State")
        zip_code = data.get("District Zip")
        website = data.get("District Web Page Address")

        district.phone_number = phone_number
        district.phone_number_extension = phone_number_extension
        district.fax_number = fax_number
        district.fax_number_extension = fax_number_extension
        district.street = street
        district.city = city
        district.state = state
        district.zip_code = zip_code
        district.website = website

        district.save()
