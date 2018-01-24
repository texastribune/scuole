# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import csv
import datetime
import os
import requests
import string

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from ...models import District, Superintendent


class Command(BaseCommand):
    help = 'Update AskTED data every day!'

    def handle(self, *args, **options):
        askted_folder = os.path.join(
            settings.DATA_FOLDER, 'askted')

        district_folder = os.path.join(
            settings.DATA_FOLDER, 'askted', 'district')

        self.superintendent_data = self.load_superintendent_directory_csv(
            district_folder)

        self.load_askted_directory_csv(askted_folder)

    def create_csv(self, filename, reader):
        with open(filename, 'w+') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in reader:
                writer.writerow(row)
                # print(row['District Name'])

    def load_askted_directory_csv(self, directory):
        url = 'http://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile.aspx'
        data = {
            '__VIEWSTATE': '/wEPDwULLTE3NDczMDI1MTIPZBYCAgEPZBYEAgMPFCsABWRkZBQrAAcQFg4eBkl0ZW1JRAURX2N0bDAtbWVudUl0ZW0wMDAeCEl0ZW1UZXh0BVI8YSBpZD0iaHlwZXJsaW5rMSIgaHJlZj0iL1RFQS5Bc2tURUQuV2ViL0Zvcm1zL0hvbWUuYXNweCIgY2xhc3M9Im1lbnVOYXYiPkhvbWU8L2E+HgdJdGVtVVJMBRF+L0Zvcm1zL0hvbWUuYXNweB4PTWVudUl0ZW1Ub29sVGlwBQRIb21lHhBNZW51SXRlbUNzc0NsYXNzBRJob3Jpem9udGFsTWVudUl0ZW0eFUl0ZW1Nb3VzZU92ZXJDc3NDbGFzcwUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB4LSXRlbVNlY3VyZWRoZGQQFgwfAAURX2N0bDAtbWVudUl0ZW0wMDEfAQVNPGEgaHJlZj0iL1RFQS5Bc2tURUQuV2ViL0Zvcm1zL1NlYXJjaE1haW4uYXNweCIgY2xhc3M9Im1lbnVOYXYiPlNlYXJjaCBieTwvYT4fAwU+U2VhcmNoIFNjcmVlbnMgZm9yIFNjaG9vbCwgRGlzdHJpY3QsIENvdW50eSwgUmVnaW9uLCBhbmQgVGV4YXMfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmgUKwAFEBYOHwAFJV9jdGwwLW1lbnVJdGVtMDAxLXN1Yk1lbnUtbWVudUl0ZW0wMDAfAQUGU2Nob29sHwIFKH4vRm9ybXMvU2VhcmNoU2NyZWVuLmFzcHg/b3JnVHlwZT1TY2hvb2wfAwUQU2VhcmNoIGJ5IFNjaG9vbB8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFJV9jdGwwLW1lbnVJdGVtMDAxLXN1Yk1lbnUtbWVudUl0ZW0wMDEfAQUIRGlzdHJpY3QfAgUqfi9Gb3Jtcy9TZWFyY2hTY3JlZW4uYXNweD9vcmdUeXBlPURpc3RyaWN0HwMFElNlYXJjaCBieSBEaXN0cmljdB8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFJV9jdGwwLW1lbnVJdGVtMDAxLXN1Yk1lbnUtbWVudUl0ZW0wMDIfAQUGQ291bnR5HwIFKH4vRm9ybXMvU2VhcmNoU2NyZWVuLmFzcHg/b3JnVHlwZT1Db3VudHkfAwUQU2VhcmNoIGJ5IENvdW50eR8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFJV9jdGwwLW1lbnVJdGVtMDAxLXN1Yk1lbnUtbWVudUl0ZW0wMDMfAQUGUmVnaW9uHwIFKH4vRm9ybXMvU2VhcmNoU2NyZWVuLmFzcHg/b3JnVHlwZT1SZWdpb24fAwUQU2VhcmNoIGJ5IFJlZ2lvbh8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFJV9jdGwwLW1lbnVJdGVtMDAxLXN1Yk1lbnUtbWVudUl0ZW0wMDQfAQUFVGV4YXMfAgUnfi9Gb3Jtcy9TZWFyY2hTY3JlZW4uYXNweD9vcmdUeXBlPVN0YXRlHwMFE1NlYXJjaCBFbnRpcmUgU3RhdGUfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZGQQFg4fAAURX2N0bDAtbWVudUl0ZW0wMDIfAQVaPGEgaHJlZj0iL1RFQS5Bc2tURUQuV2ViL0Zvcm1zL1F1aWNrU2VhcmNoLmFzcHgiIGNsYXNzPSJtZW51TmF2Ij5RdWljayBEaXN0cmljdCBMb29rdXA8L2E+HwIFGH4vRm9ybXMvUXVpY2tTZWFyY2guYXNweB8DBRVRdWljayBEaXN0cmljdCBMb29rdXAfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDB8ABRFfY3RsMC1tZW51SXRlbTAwMx8BBVs8YSBocmVmPSIvVEVBLkFza1RFRC5XZWIvRm9ybXMvUmVwb3J0TWFpbi5hc3B4IiBjbGFzcz0ibWVudU5hdiI+UmVwb3J0cyBhbmQgRGlyZWN0b3JpZXM8L2E+HwMFU1JlcG9ydHMgYW5kIERpcmVjdG9yaWVzIC0gUmVwb3J0cywgRG93bmxvYWQgRGF0YSBGaWxlcyBhbmQgVGV4YXMgU2Nob29sIERpcmVjdG9yaWVzHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoFCsABBAWDh8ABSVfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAwHwEFB1JlcG9ydHMfAgUcfi9Gb3Jtcy9SZXBvcnRTZWxlY3Rpb24uYXNweB8DBRJQcmVkZWZpbmVkIFJlcG9ydHMfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABSVfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAxHwEFJkRvd25sb2FkIFNjaG9vbCBhbmQgRGlzdHJpY3QgRGF0YSBGaWxlHwIFGX4vRm9ybXMvRG93bmxvYWRGaWxlLmFzcHgfAwUmRG93bmxvYWQgU2Nob29sIGFuZCBEaXN0cmljdCBEYXRhIEZpbGUfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABSVfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAyHwEFNURvd25sb2FkIFNjaG9vbCwgRGlzdHJpY3QgYW5kIEVTQyBQZXJzb25uZWwgRGF0YSBGaWxlHwIFGn4vRm9ybXMvRG93bmxvYWRGaWxlMi5hc3B4HwMFSURvd25sb2FkIFByaW5jaXBhbHMsIFN1cGVyaW50ZW5kZW50cywgRGlzdHJpY3QgYW5kL29yIEVTQyBTdGFmZiBEYXRhIEZpbGUfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDB8ABSVfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzHwEFGFRleGFzIFNjaG9vbCBEaXJlY3Rvcmllcx8DBTZQdWJsaXNoZWQgSGlzdG9yaWNhbCBUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IC5wZGYgZmlsZXMfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmgUKwAdEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMB8BBQsyMDE2IC0gMjAxNx8CBRl+L0Zvcm1zL3RzZGluZGV4MjAxNy5hc3B4HwMFIlRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAxNiAtIDIwMTcfBAUSaG9yaXpvbnRhbG1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDEfAQUhMjAxNiAtIDIwMTcgc2NyZWVuIHJlYWRlciBlbmFibGVkHwIFH34vRm9ybXMvdHNkaW5kZXgyMDE3dGFnZ2VkLmFzcHgfAwU4VGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDE2IC0gMjAxNyBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDIfAQULMjAxNSAtIDIwMTYfAgUZfi9Gb3Jtcy90c2RpbmRleDIwMTYuYXNweB8DBSJUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMTUgLSAyMDE2HwQFEmhvcml6b250YWxtZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzHwEFITIwMTUgLSAyMDE2IHNjcmVlbiByZWFkZXIgZW5hYmxlZB8CBR9+L0Zvcm1zL3RzZGluZGV4MjAxNnRhZ2dlZC5hc3B4HwMFOFRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAxNSAtIDIwMTYgc2NyZWVuIHJlYWRlciBlbmFibGVkHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDA0HwEFCzIwMTQgLSAyMDE1HwIFGX4vRm9ybXMvdHNkaW5kZXgyMDE1LmFzcHgfAwUiVGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDE0IC0gMjAxNR8EBRJob3Jpem9udGFsbWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwNR8BBSEyMDE0IC0gMjAxNSBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfAgUffi9Gb3Jtcy90c2RpbmRleDIwMTV0YWdnZWQuYXNweB8DBThUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMTQgLSAyMDE1IHNjcmVlbiByZWFkZXIgZW5hYmxlZB8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwNh8BBQsyMDEzIC0gMjAxNB8CBRl+L0Zvcm1zL3RzZGluZGV4MjAxNC5hc3B4HwMFIlRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAxMyAtIDIwMTQfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDcfAQUhMjAxMyAtIDIwMTQgc2NyZWVuIHJlYWRlciBlbmFibGVkHwIFH34vRm9ybXMvdHNkaW5kZXgyMDE0dGFnZ2VkLmFzcHgfAwU4VGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDEzIC0gMjAxNCBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDgfAQULMjAxMiAtIDIwMTMfAgUZfi9Gb3Jtcy90c2RpbmRleDIwMTMuYXNweB8DBSJUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMTIgLSAyMDEzHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDA5HwEFITIwMTIgLSAyMDEzIHNjcmVlbiByZWFkZXIgZW5hYmxlZB8CBR9+L0Zvcm1zL3RzZGluZGV4MjAxM3RhZ2dlZC5hc3B4HwMFOFRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAxMiAtIDIwMTMgc2NyZWVuIHJlYWRlciBlbmFibGVkHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDEwHwEFCzIwMTEgLSAyMDEyHwIFGX4vRm9ybXMvdHNkaW5kZXgyMDEyLmFzcHgfAwUiVGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDExIC0gMjAxMh8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAxMR8BBSEyMDExIC0gMjAxMiBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfAgUffi9Gb3Jtcy90c2RpbmRleDIwMTJ0YWdnZWQuYXNweB8DBThUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMTEgLSAyMDEyIHNjcmVlbiByZWFkZXIgZW5hYmxlZB8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAxMh8BBQsyMDEwIC0gMjAxMR8CBRl+L0Zvcm1zL3RzZGluZGV4MjAxMS5hc3B4HwMFIlRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAxMCAtIDIwMTEfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMTMfAQUhMjAxMCAtIDIwMTEgc2NyZWVuIHJlYWRlciBlbmFibGVkHwIFH34vRm9ybXMvdHNkaW5kZXgyMDExdGFnZ2VkLmFzcHgfAwU4VGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDEwIC0gMjAxMSBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMTQfAQULMjAwOSAtIDIwMTAfAgUZfi9Gb3Jtcy90c2RpbmRleDIwMTAuYXNweB8DBSJUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMDkgLSAyMDEwHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDE1HwEFITIwMDkgLSAyMDEwIHNjcmVlbiByZWFkZXIgZW5hYmxlZB8CBR9+L0Zvcm1zL3RzZGluZGV4MjAxMHRhZ2dlZC5hc3B4HwMFOFRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAwOSAtIDIwMTAgc2NyZWVuIHJlYWRlciBlbmFibGVkHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDE2HwEFCzIwMDggLSAyMDA5HwIFGX4vRm9ybXMvdHNkaW5kZXgyMDA5LmFzcHgfAwUiVGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDA4IC0gMjAwOR8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAxNx8BBSEyMDA4IC0gMjAwOSBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfAgUffi9Gb3Jtcy90c2RpbmRleDIwMDl0YWdnZWQuYXNweB8DBThUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMDggLSAyMDA5IHNjcmVlbiByZWFkZXIgZW5hYmxlZB8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAxOB8BBQsyMDA3IC0gMjAwOB8CBRl+L0Zvcm1zL3RzZGluZGV4MjAwOC5hc3B4HwMFIlRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAwNyAtIDIwMDgfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMTkfAQUhMjAwNyAtIDIwMDggc2NyZWVuIHJlYWRlciBlbmFibGVkHwIFH34vRm9ybXMvdHNkaW5kZXgyMDA4dGFnZ2VkLmFzcHgfAwU4VGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDA3IC0gMjAwOCBzY3JlZW4gcmVhZGVyIGVuYWJsZWQfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMjAfAQULMjAwNiAtIDIwMDcfAgUZfi9Gb3Jtcy90c2RpbmRleDIwMDcuYXNweB8DBSJUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMDYgLSAyMDA3HwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDIxHwEFITIwMDYgLSAyMDA3IHNjcmVlbiByZWFkZXIgZW5hYmxlZB8CBR9+L0Zvcm1zL3RzZGluZGV4MjAwN3RhZ2dlZC5hc3B4HwMFOFRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAwNiAtIDIwMDcgc2NyZWVuIHJlYWRlciBlbmFibGVkHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDIyHwEFCzIwMDUgLSAyMDA2HwIFGX4vRm9ybXMvdHNkaW5kZXgyMDA2LmFzcHgfAwUiVGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDA1IC0gMjAwNh8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAyMx8BBQsyMDA0IC0gMjAwNR8CBRl+L0Zvcm1zL3RzZGluZGV4MjAwNS5hc3B4HwMFIlRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAwNCAtIDIwMDUfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMjQfAQULMjAwMyAtIDIwMDQfAgUZfi9Gb3Jtcy90c2RpbmRleDIwMDQuYXNweB8DBSJUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMDMgLSAyMDA0HwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDI1HwEFCzIwMDIgLSAyMDAzHwIFGX4vRm9ybXMvdHNkaW5kZXgyMDAzLmFzcHgfAwUiVGV4YXMgU2Nob29sIERpcmVjdG9yeSAyMDAyIC0gMjAwMx8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkEBYOHwAFOV9jdGwwLW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAyNh8BBQsyMDAxIC0gMjAwMh8CBRl+L0Zvcm1zL3RzZGluZGV4MjAwMi5hc3B4HwMFIlRleGFzIFNjaG9vbCBEaXJlY3RvcnkgMjAwMSAtIDIwMDIfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWDh8ABTlfY3RsMC1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDAzLXN1Yk1lbnUtbWVudUl0ZW0wMjcfAQULMjAwMCAtIDIwMDEfAgUZfi9Gb3Jtcy90c2RpbmRleDIwMDEuYXNweB8DBSJUZXhhcyBTY2hvb2wgRGlyZWN0b3J5IDIwMDAgLSAyMDAxHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFg4fAAU5X2N0bDAtbWVudUl0ZW0wMDMtc3ViTWVudS1tZW51SXRlbTAwMy1zdWJNZW51LW1lbnVJdGVtMDI4HwEFCzE5OTkgLSAyMDAwHwIFGX4vRm9ybXMvdHNkaW5kZXgyMDAwLmFzcHgfAwUiVGV4YXMgU2Nob29sIERpcmVjdG9yeSAxOTk5IC0gMjAwMB8EBRJob3Jpem9udGFsTWVudUl0ZW0fBQUWaG9yaXpvbnRhbE1lbnVTZWxlY3RlZB8GaGRkZGQQFg4fAAURX2N0bDAtbWVudUl0ZW0wMDQfAQVVPGEgaHJlZj0iL1RFQS5Bc2tURUQuV2ViL0Zvcm1zL0VTQ1NlYXJjaFNjcmVlbi5hc3B4IiBjbGFzcz0ibWVudU5hdiI+U2VhcmNoIFJFU0NzPC9hPh8CBRx+L0Zvcm1zL0VTQ1NlYXJjaFNjcmVlbi5hc3B4HwMFKVNlYXJjaCBSZWdpb25hbCBFZHVjYXRpb24gU2VydmljZSBDZW50ZXJzHwQFEmhvcml6b250YWxNZW51SXRlbR8FBRZob3Jpem9udGFsTWVudVNlbGVjdGVkHwZoZGQQFhAfAAURX2N0bDAtbWVudUl0ZW0wMDUfAQUyPGEgaHJlZj0jIGNsYXNzPSJtZW51TmF2Ij5BZG1pbmlzdHJhdGl2ZSBMb2dvbjwvYT4fAgUtaHR0cHM6Ly9zZWd1aW4udGVhLnN0YXRlLnR4LnVzL2FwcHMvbG9nb24uYXNwHgpJdGVtVGFyZ2V0BQZfYmxhbmsfAwUaQWRtaW5pc3RyYXRpdmUgUGFnZSBBY2Nlc3MfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBAWEB8ABRFfY3RsMC1tZW51SXRlbTAwNh8BBSI8YSBocmVmPSMgY2xhc3M9Im1lbnVOYXYiPkhlbHA8L2E+HwIFFX4vaGVscC9hc2t0ZWRfbmV3Lmh0bR8HBQZfYmxhbmsfAwURQXNrVEVEIFF1aWNrIEhlbHAfBAUSaG9yaXpvbnRhbE1lbnVJdGVtHwUFFmhvcml6b250YWxNZW51U2VsZWN0ZWQfBmhkZBQrAAEFB3RlYXRlbXBkAg0PEGQPFglmAgECAgIDAgQCBQIGAgcCCBYJEAUNU2Nob29sIE51bWJlcgUNU2Nob29sIE51bWJlcmcQBQtTY2hvb2wgTmFtZQULU2Nob29sIE5hbWVnEAUNRGlzdHJpY3QgTmFtZQUNRGlzdHJpY3QgTmFtZWcQBQtDb3VudHkgTmFtZQULQ291bnR5IE5hbWVnEAUGUmVnaW9uBQZSZWdpb25nEAULU2Nob29sIENpdHkFC1NjaG9vbCBDaXR5ZxAFD1NjaG9vbCBaaXAgQ29kZQUPU2Nob29sIFppcCBDb2RlZxAFDURpc3RyaWN0IENpdHkFDURpc3RyaWN0IENpdHlnEAURRGlzdHJpY3QgWmlwIENvZGUFEURpc3RyaWN0IFppcCBDb2RlZ2RkZAwB4wuMbc+K5oXsH9/Cx3qA59mu',
            '__VIEWSTATEGENERATOR': '44F2C40C',
            'ddlSortOrder': 'School+Number',
            'btnDownloadFile': 'Download+File',
        }

        req = requests.post(url, data=data)
        reader = csv.DictReader(req.text.splitlines())
        fieldnames = [
            'School Name',
            'Instruction Type',
            'School State',
            'District Superintendent',
            'School Status Date',
            'School Email Address',
            'School Number',
            'Region Number',
            'County Number',
            'County Name',
            'District Email Address',
            'District Number',
            'Update Date',
            'District City',
            'School Enrollment as of Oct 2016',
            'School Zip',
            'School Principal',
            'School Fax',
            'District Web Page Address',
            'District Street Address',
            'District Fax',
            'School Phone',
            'District Enrollment as of Oct 2016',
            'Grade Range',
            'School Status',
            'District Name',
            'School Web Page Address',
            'School Street Address',
            'District Zip',
            'District State',
            'District Type',
            'Charter Type',
            'District Phone',
            'School City',
        ]

        date = str(datetime.datetime.now().date())
        directoryFilename = directory + '/' + date + '_askTedDirectory.csv'
        directoryFile = os.path.join(
            settings.DATA_FOLDER, 'askted', date + '_askTedDirectory.csv')
        isDirectoryFile = os.path.isfile(directoryFilename)

        if not isDirectoryFile:
            with open(directoryFilename, 'w+') as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)
        else:
            print("We already have today's district data! Moving on...")

        with open(directoryFile, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.update_district(row)

    def update_district(self, district):
        # askTed districts have apostrophes in them
        district_id = str(district['District Number']).replace("'", "")
        district_name = district['District Name']
        # if there's a district already in the databasa, match this askTed data
        # to that TAPR data. Otherwise, move on
        try:
            district_match = District.objects.get(tea_id=district_id)

            phone_number = district['District Phone']
            fax_number = district['District Fax']
            # sometimes phone and fax numbers have extensions at the end
            # this splits out the extension into its own field
            if 'ext' in phone_number:
                phone_number, phone_number_extension = phone_number.split(' ext:')
                phone_number_extension = str(phone_number_extension)
            else:
                phone_number_extension = ''

            if 'ext' in fax_number:
                fax_number, fax_number_extension = fax_number.split(' ext:')
                fax_number_extension = str(phone_number_extension)
            else:
                fax_number_extension = ''

            # update all of the askTed district fields and save it to the model
            district_match.phone_number = phone_number
            district_match.phone_number_extension = phone_number_extension
            district_match.fax_number = fax_number
            district_match.fax_number_extension = fax_number_extension
            district_match.street = district['District Street Address']
            district_match.city = district['District City']
            district_match.state = district['District State']
            district_match.zip_code = district['District Zip']
            district_match.website = district['District Web Page Address']
            district_match.save()

            superintendent = self.superintendent_data[district_id]
            self.create_superintendent(district_match, superintendent)

            self.stdout.write('Creating {}...'.format(district_name))
        except ObjectDoesNotExist:
            self.stderr.write('No askted data for {}'.format(district_name))

    def load_superintendent_directory_csv(self, file):
        # url where general directory lives
        url = 'http://tea4avholly.tea.state.tx.us/TEA.AskTED.Web/Forms/DownloadFile2.aspx'
        # request params
        data = {
            '__VIEWSTATE': '',
            '__VIEWSTATEGENERATOR': '3B1DF71D',
            'chkSuper': 'on',
            'lstDistrictStaff': '0',
            'lstESCStaff': '0',
            'ddlSortOrder': 'Organization+Name',
            'btnDownloadFile': 'Download+File',
        }
        fieldnames = [
            'Charter Type',
            'Email Address',
            'Organization Name',
            'Full Name',
            'Role',
            'Fax',
            'State',
            'District Name',
            'Organization Number',
            'First Name',
            'Last Name',
            'Organization SubType',
            'County Number',
            'Street Address',
            'Zip',
            'Region Number',
            'Salutation Title',
            'Phone',
            'Organization Type',
            'County Name',
            'City',
            'District Number',
        ]
        req = requests.post(url, data=data)
        reader = csv.DictReader(req.text.splitlines())
        date = str(datetime.datetime.now().date())
        superintendentFilename = file + '/' + date + '_askTedSuperindendent.csv'
        isSuperintendentFile = os.path.isfile(superintendentFilename)

        if not isSuperintendentFile:
            with open(superintendentFilename, 'w+') as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    writer.writerow(row)

        superintendent_csv = os.path.join(settings.DATA_FOLDER, 'askted', 'district', date + '_askTedSuperindendent.csv')

        payload = {}

        with open(superintendent_csv, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tea_id = row['District Number'].replace("'", "")
                payload[tea_id] = row

        return payload

    def create_superintendent(self, district, superintendent):

        name = '{} {}'.format(
            superintendent['First Name'], superintendent['Last Name'])
        name = string.capwords(name)
        phone_number = superintendent['Phone']
        fax_number = superintendent['Fax']

        if 'ext' in phone_number:
            phone_number, phone_number_extension = phone_number.split(' ext:')
            phone_number_extension = str(phone_number_extension)
        else:
            phone_number_extension = ''

        if 'ext' in fax_number:
            fax_number, fax_number_extension = fax_number.split(' ext:')
            fax_number_extension = str(phone_number_extension)
        else:
            fax_number_extension = ''
        # unlike the district model we're updating above, the superintendent
        # model doesn't exist yet- so we're creating it here
        instance, _ = Superintendent.objects.update_or_create(
            name=name,
            district=district,
            defaults={
                'role': superintendent['Role'],
                'email': superintendent['Email Address'],
                'phone_number': phone_number,
                'phone_number_extension': phone_number_extension,
                'fax_number': fax_number,
                'fax_number_extension': fax_number_extension,
            }
        )
