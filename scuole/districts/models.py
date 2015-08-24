# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from localflavor.us.models import USStateField, USZipCodeField

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.counties.models import County
from scuole.regions.models import Region
from scuole.stats.models import SchoolYear, StatsBase


@python_2_unicode_compatible
class District(models.Model):
    # CCD - NAME
    name = models.CharField('District name', max_length=200)
    slug = models.SlugField(max_length=75)
    # TEA - STID
    tea_id = models.CharField('TEA district identifier', max_length=6)
    # CCD - LSTREE
    street = models.CharField('District street', max_length=200)
    # CCD - LCITY
    city = models.CharField('District office city', max_length=100)
    # CCD - LSTATE
    state = USStateField(
        'District office abbreviated state location', max_length=2)
    # CCD - LZIP-LZIP4
    zip_code = USZipCodeField('District ZIP Code')
    # CCD - LATCOD
    latitude = models.FloatField('District office latitude')
    # CCD - LONCOD
    longitude = models.FloatField('District office longitude')
    region = models.ForeignKey(
        Region, related_name='districts', null=True, blank=True)
    county = models.ForeignKey(
        County, related_name='districts', null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class DistrictStats(StatsBase):
    district = models.ForeignKey(District, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='district_stats')

    class Meta:
        unique_together = ('district', 'year',)
        verbose_name_plural = 'District stats'

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.district.name)
