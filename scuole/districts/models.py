from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class District(models.Model):
    # CCD district data #
    # NAME
    name = models.CharField(
        help_text='District name', max_length=200)
    slug = models.SlugField()
    # STID
    tea_id = models.CharField(
        help_text='TEA district identifier',
        max_length=6)
    # LSTREE
    street = models.CharField(
        help_text='District street',
        max_length=200)
    # LCITY
    city = models.CharField(
        help_text='District office city',
        max_length=100)
    # LSTATE
    state = models.CharField(
        help_text='District office abbreviated state location',
        max_length=2)
    # LZIP
    zip_code = models.CharField(
        help_text='District office ZIP Code',
        max_length=5)
    # LZIP4
    zip_code4 = models.CharField(
        help_text='District office +4 ZIP Code',
        max_length=4)
    # LATCOD
    latitude = models.FloatField(help_text='District office latitude')
    # LONCOD
    longitude = models.FloatField(help_text='District office longitude')

    def __str__(self):
        return self.name
