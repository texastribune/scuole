# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.districts.models import District


@python_2_unicode_compatible
class Campus(models.Model):
    # CCD - SCHNAM
    name = models.CharField(
        help_text="Campus name", max_length=200)
    slug = models.SlugField()
    # TEA - CAMPUS
    tea_id = models.CharField(
        help_text="TEA campus identifier",
        max_length=10)
    # CCD - PHONE
    phone = models.CharField(
        help_text="Campus phone number",
        max_length=10)
    # CCD - LSTREE
    street = models.CharField(
        help_text="Campus location street",
        max_length=100)
    # CCD - LCITY
    city = models.CharField(
        help_text="Campus location city",
        max_length=200)
    # CCD - LSTREE
    street = models.CharField(
        help_text="Campus location street address",
        max_length=200)
    # CCD - LSTATE
    state = models.CharField(
        help_text="Campus location state",
        max_length=5)
    # CCD - LZIP
    zip_code = models.CharField(
        help_text="Campus location zip",
        max_length=5)
    # CCD - LZIP4
    zip_code4 = models.CharField(
        help_text="Campus +4 zip",
        max_length=4)
    #CCD - STATUS
    status = models.CharField(
        help_text="Campus NCES status code",
        max_length=1)
    # CCD - ULOCALE
    locale = models.CharField(
        help_text="Campus NCES urban-centric locale code",
        max_length=2)
    # CCD - LATCOD
    latitude = models.FloatField(help_text="Campus latitude")
    # CCD - LONCOD
    longitude = models.FloatField(help_text="Campus longitude")
    district = models.ForeignKey(
        District, related_name="campuses")

    def __str__(self):
        return self.name
