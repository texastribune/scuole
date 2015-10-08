# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import string

from localflavor.us.models import USStateField, USZipCodeField

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.counties.models import County
from scuole.regions.models import Region
from scuole.stats.models import SchoolYear, StatsBase


@python_2_unicode_compatible
class District(models.Model):
    MET_STANDARD = 'M'
    MET_ALTERNATIVE_STANDARD = 'A'
    IMPROVEMENT_REQUIRED = 'I'
    NOT_RATED = 'X'
    NOT_RATED = 'Z'
    NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE = 'Q'

    RATING_CHOICES = (
        (MET_STANDARD, 'Met standard'),
        (MET_ALTERNATIVE_STANDARD, 'Met alternative standard'),
        (IMPROVEMENT_REQUIRED, 'Improvement required'),
        (NOT_RATED, 'Not rated'),
        (NOT_RATED_DUE_TO_DATA_INTEGRITY_ISSUE,
            'Not rated due to data integrity issue'),
    )

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
    region = models.ForeignKey(
        Region, related_name='districts', null=True, blank=True)
    county = models.ForeignKey(
        County, related_name='districts', null=True, blank=True)
    accountability_rating = models.CharField(
        'Accountability rating', max_length=1, choices=RATING_CHOICES
    )
    # CCD - LONCOD, LATCOD
    coordinates = models.PointField('District office coordinates', null=True)
    shape = models.MultiPolygonField('District shape', srid=4326, null=True)

    objects = models.GeoManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('districts:detail', kwargs={
            'district_slug': self.slug,
            'district_id': self.pk,
        })

    @property
    def location(self):
        return '{city}, {state}'.format(
            city=string.capwords(self.city),
            state=self.state)


@python_2_unicode_compatible
class DistrictStats(StatsBase):
    district = models.ForeignKey(District, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='district_stats')

    class Meta:
        unique_together = ('district', 'year',)
        verbose_name_plural = 'District stats'

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.district.name)
