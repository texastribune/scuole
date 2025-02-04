from csv import DictReader

import requests

from django.core.management.base import BaseCommand

from scuole.campuses.models import Campus
from scuole.core.constants import ASKTED_DIRECTORY_URL, ASKTED_DIRECTORY_VIEWSTATE

def phoneNumberFormat(number):
    if number == ' ' or '000-0000' in number:
        return ''
    else:
        return number.replace('(000) 000-0000','')


class Command(BaseCommand):
    help = "Update Campus models with AskTED data."

    def handle(self, *args, **options):
        # track the ones we've seen so far so we don't waste time
        self.processed_campuses = set()

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
            self.update_campus(row)

    def update_campus(self, data):
        # AskTED campus IDs have apostrophes in them, strangely
        campus_id = data.get("School Number").replace("'", "").zfill(9)

        if campus_id in self.processed_campuses:
            return

        self.processed_campuses.add(campus_id)

        try:
            campus = Campus.objects.get(tea_id=campus_id)
        except Campus.DoesNotExist:
            # if there's no match don't worry about it
            return

        self.stdout.write(f"Updating AskTED data for {campus.name} ({campus_id})")

        phone_number = data.get("School Phone")
        fax_number = data.get("School Fax")

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

        street = data.get("School Site Street Address")
        city = data.get("School Site City")
        state = data.get("School Site State")
        zip_code = data.get("School Site Zip")
        website = data.get("School Web Page Address")

        # This accounts for invalid phone numbers
        # print(phone_number)
        # print(fax_number)
        # print('-')
        phone_number = phoneNumberFormat(phone_number)
        fax_number = phoneNumberFormat(fax_number)
        # print(phone_number)
        # print(fax_number)
        # print('---')

        campus.phone_number = phone_number
        campus.phone_number_extension = phone_number_extension
        campus.fax_number = fax_number
        campus.fax_number_extension = fax_number_extension
        campus.street = street
        campus.city = city
        campus.state = state
        campus.zip_code = zip_code
        campus.website = website

        campus.save()
