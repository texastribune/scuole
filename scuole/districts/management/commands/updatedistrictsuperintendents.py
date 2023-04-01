from csv import DictReader
from string import capwords

import requests

from django.core.management.base import BaseCommand

from scuole.core.constants import ASKTED_PERSONNEL_URL, ASKTED_PERSONNEL_VIEWSTATE
from scuole.districts.models import District, Superintendent
from scuole.core.utils import nameFormat

def phoneNumberFormat(number):
    if number is ' ' or '000-0000' in number:
        return ''
    else:
        return number.replace('(000) 000-0000','')\
                        .replace('(993)','(936)')

class Command(BaseCommand):
    help = "Update District models with AskTED superintendent data."

    def handle(self, *args, **options):
        # Downloads data directly from AskTED site
        # https://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx
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

    
        name = capwords(nameFormat(data.get("District Superintendent").strip()))

        role = "Superintendent"
        email = data.get("District Email Address")
        phone_number = data.get("District Phone")
        fax_number = data.get("District Fax")

        if "ext" in phone_number:
            phone_number, phone_number_extension = phone_number.split(" ext:")
        else:
            phone_number_extension = ""

        if "ext" in fax_number:
            fax_number, fax_number_extension = fax_number.split(" ext:")
        else:
            fax_number_extension = ""

        # This accounts for invalid phone numbers

        # print(phone_number)
        # print(fax_number)
        # print('-')\
        phone_number = phoneNumberFormat(phone_number)
        fax_number = phoneNumberFormat(fax_number)
        # print(phone_number)
        # print(fax_number)
        # print('---')

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
