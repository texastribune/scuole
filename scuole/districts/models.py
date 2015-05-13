from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.counties.models import County
from scuole.regions.models import Region


@python_2_unicode_compatible
class District(models.Model):
    # CCD - NAME
    name = models.CharField(
        help_text='District name', max_length=200)
    slug = models.SlugField(max_length=75)
    # TEA - STID
    tea_id = models.CharField(
        help_text='TEA district identifier',
        max_length=6)
    # CCD - LSTREE
    street = models.CharField(
        help_text='District street',
        max_length=200)
    # CCD - LCITY
    city = models.CharField(
        help_text='District office city',
        max_length=100)
    # CCD - LSTATE
    state = models.CharField(
        help_text='District office abbreviated state location',
        max_length=2)
    # CCD - LZIP
    zip_code = models.CharField(
        help_text='District office ZIP Code',
        max_length=5)
    # CCD - LZIP4
    zip_code4 = models.CharField(
        help_text='District office +4 ZIP Code',
        max_length=4)
    # CCD - LATCOD
    latitude = models.FloatField(help_text='District office latitude')
    # CCD - LONCOD
    longitude = models.FloatField(help_text='District office longitude')
    region = models.ForeignKey(
        Region, related_name='districts', null=True, blank=True)
    county = models.ForeignKey(
        County, related_name='districts', null=True, blank=True)

    def __str__(self):
        return self.name
