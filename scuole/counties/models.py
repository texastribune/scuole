# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property

from scuole.stats.models import SchoolYear
from scuole.states.models import State
from scuole.cohorts.models import CohortsBase
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class County(models.Model):
    name = models.CharField(_('County name'), max_length=100)
    slug = models.SlugField()
    fips = models.CharField(_('County FIPS place code'), max_length=3)
    shape = models.MultiPolygonField(_('Region shape'), srid=4326, null=True)
    state = models.ForeignKey(State, related_name=_('counties'))

    class Meta:
        verbose_name_plural = _('counties')

    def __str__(self):
        return self.name

    @property
    def name_full(self):
        return '{0} County'.format(self.name)

    @cached_property
    def shape_simple(self):
        return self.shape.simplify(0.01)


@python_2_unicode_compatible
class CountyCohorts(CohortsBase):
    county = models.ForeignKey(County, related_name='cohorts')
    year = models.ForeignKey(SchoolYear, related_name='county_cohorts')

    class Meta:
        unique_together = (
            'county', 'year', 'economic_status', 'gender', 'ethnicity')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.county.name)
