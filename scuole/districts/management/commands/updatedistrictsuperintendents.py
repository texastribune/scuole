from csv import DictReader
from string import capwords

import requests

from django.core.management.base import BaseCommand

from scuole.core.constants import ASKTED_PERSONNEL_URL, ASKTED_PERSONNEL_VIEWSTATE
from scuole.districts.models import District, Superintendent


class Command(BaseCommand):
    help = "Update District models with AskTED superintendent data."

    def handle(self, *args, **options):
        req = requests.post(
            ASKTED_PERSONNEL_URL,
            data={
                "__VIEWSTATE": ASKTED_PERSONNEL_VIEWSTATE,
                "chkSuper": "on",
                "lstDistrictStaff": "0",
                "lstESCStaff": "0",
                "ddlSortOrder": "Organization Number",
                "btnDownloadFile": "Download File",
            },
        )

        directory_data = DictReader(req.text.splitlines())

        for row in directory_data:
            self.create_or_update_superintendent(row)

    def create_or_update_superintendent(self, data):
        # AskTED districts have apostrophes in them, strangely
        district_id = data.get("District Number").replace("'", "").zfill(6)

        try:
            district = District.objects.get(tea_id=district_id)
        except District.DoesNotExist:
            # if there's no match don't worry about it
            return

        self.stdout.write(
            f"Updating superintendent data for {district.name} ({district_id})"
        )

        first_name = data.get("First Name").strip()
        last_name = data.get("Last Name").strip()
        name = capwords(f"{first_name} {last_name}")

        role = capwords(data.get("Role"))
        email = data.get("Email Address")
        phone_number = data.get("Phone")
        fax_number = data.get("Fax")

        if "ext" in phone_number:
            phone_number, phone_number_extension = phone_number.split(" ext:")
        else:
            phone_number_extension = ""

        if "ext" in fax_number:
            fax_number, fax_number_extension = fax_number.split(" ext:")
        else:
            fax_number_extension = ""

        Superintendent.objects.update_or_create(
            name=name,
            district=district,
            defaults={
                "role": role,
                "email": email,
                "phone_number": phone_number,
                "phone_number_extension": phone_number_extension,
                "fax_number": fax_number,
                "fax_number_extension": fax_number_extension,
            },
        )
