# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import string

from django.contrib.gis.db import models
from django.core.serializers import serialize
from django.utils.translation import ugettext_lazy as _

from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField

from scuole.core.models import PersonnelBase
from scuole.counties.models import County
from scuole.regions.models import Region
from scuole.stats.models import ReferenceBase, SchoolYear, StatsBase


class District(models.Model):
    name = models.CharField(_('District name'), max_length=200)
    slug = models.SlugField(max_length=75)
    # TEA - STID
    tea_id = models.CharField(_('TEA district identifier'), max_length=6)
    phone_number = PhoneNumberField(
        _('District phone number'), max_length=20, null=True
    )
    phone_number_extension = models.CharField(
        _('Phone number extension'), max_length=4, blank=True, default=''
    )
    website = models.URLField(_('District website'), blank=True, default='')
    charter = models.BooleanField(_('Charter status'), default=False)
    street = models.CharField(_('District street'), max_length=200)
    city = models.CharField(_('District office city'), max_length=100)
    state = USStateField(_('District office abbreviated state location'), max_length=2)
    zip_code = USZipCodeField(_('District ZIP Code'))
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='districts',
        null=True,
        blank=True,
    )
    county = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        related_name='districts',
        null=True,
        blank=True,
    )
    shape = models.MultiPolygonField(_('District shape'), srid=4326, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse('districts:detail', kwargs={'district_slug': self.slug})

    @property
    def city_display(self):
        if self.city:
            return string.capwords(self.city)
        else:
            return ''

    @property
    def location(self):
        if self.city and self.state:
            return '{city}, {state}'.format(
                city=string.capwords(self.city), state=self.state
            )
        else:
            return ''

    @property
    def location_full(self):
        if self.city and self.state:
            return '{city}, {state}'.format(
                city=string.capwords(self.city), state=self.get_state_display()
            )
        else:
            return ''

    @property
    def simple_shape(self):
        """
        Returns the district's shape with a bit of simplification so it's
        smaller.
        """
        if not self.shape:
            return None

        return self.shape.simplify(0.0001, preserve_topology=True)

    @property
    def campus_geojson(self):
        return serialize(
            'geojson', self.campuses.all(), fields=('name', 'coordinates', 'slug')
        )

    @property
    def nearby_districts(self):
        if self.shape:
            return District.objects.filter(shape__touches=self.shape)

        return None


class DistrictStats(StatsBase, ReferenceBase):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name='stats'
    )
    year = models.ForeignKey(
        SchoolYear, on_delete=models.CASCADE, related_name='district_stats'
    )

    class Meta:
        unique_together = ('district', 'year')
        verbose_name_plural = _('District stats')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.district.name)


class Superintendent(PersonnelBase):
    district = models.OneToOneField(
        District, on_delete=models.CASCADE, related_name='superintendent_of'
    )

    def __str__(self):
        return '{} at {}'.format(self.name, self.district.name)
