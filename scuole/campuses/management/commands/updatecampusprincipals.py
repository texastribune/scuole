from csv import DictReader
from string import capwords

import requests

from django.core.management.base import BaseCommand

from scuole.campuses.models import Campus, Principal
from scuole.core.constants import ASKTED_PERSONNEL_URL, ASKTED_PERSONNEL_VIEWSTATE

from scuole.core.utils import nameFormat, addComma

def phoneNumberFormat(number):
    if number is ' ' or '000-0000' in number:
        return ''
    else:
        return number.replace('(000) 000-0000','')\
                        .replace('(993)','(936)')\
                        .replace('(173)','(713)')\
                        .replace('(942)','(972)')\
                        .replace('(291)','(281)')\
                        .replace('(230)','(210)')\
                        .replace('(656)','(956)')\
                        .replace('(396)','(956)')

class Command(BaseCommand):
    help = "Update Campus models with AskTED principal data."

    def handle(self, *args, **options):
        # track the principals we added so we can remove old ones
        self.current_principals = set()

        req = requests.post(
            ASKTED_PERSONNEL_URL,
            data={
                "__VIEWSTATE": ASKTED_PERSONNEL_VIEWSTATE,
                "chkPrin": "on",
                "lstDistrictStaff": "0",
                "lstESCStaff": "0",
                "ddlSortOrder": "Organization Number",
                "btnDownloadFile": "Download File",
            },
        )

        directory_data = DictReader(req.text.splitlines())

        for row in directory_data:
            self.create_or_update_principal(row)

        # unflag all the principals who didn't get created/updated
        total_unflagged = (
            Principal.objects.exclude(id__in=self.current_principals)
            .filter(is_active=True)
            .update(is_active=False)
        )

        self.stdout.write(
            f"{total_unflagged} principal{'' if total_unflagged == 1 else 's'} marked as no longer active."
        )

    def create_or_update_principal(self, data):
        # AskTED campus IDs have apostrophes in them, strangely
        campus_id = data.get("School Number").replace("'", "").zfill(6)

        try:
            campus = Campus.objects.get(tea_id=campus_id)
        except Campus.DoesNotExist:
            # if there's no match don't worry about it
            return

        self.stdout.write(f"Updating principal data for {campus.name} ({campus_id})")
        # uses addComma function to add a comma for each principal since they are now in the same line
        names_sep = addComma(data.get("School Principal").strip())

        # Takes out the MS, MRS, MR, and DR in front of names using nameFormat function
        name = capwords(nameFormat(names_sep))

        role = "Principal"
        email = data.get("School Email Address")
        phone_number = data.get("School Phone")
        fax_number = data.get("School Fax")

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
        # print('-')
        phone_number = phoneNumberFormat(phone_number)
        fax_number = phoneNumberFormat(fax_number)
        # print(phone_number)
        # print(fax_number)
        # print('---')

        instance, _ = Principal.objects.update_or_create(
            name=name,
            campus=campus,
            defaults={
                "role": role,
                "email": email,
                "phone_number": phone_number,
                "phone_number_extension": phone_number_extension,
                "fax_number": fax_number,
                "fax_number_extension": fax_number_extension,
                "is_active": True,
            },
        )

        self.current_principals.add(instance.id)
