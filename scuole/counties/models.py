# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.gis.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from scuole.cohorts.models import CohortsBase
from scuole.states.models import State
from scuole.stats.models import SchoolYear


class County(models.Model):
    name = models.CharField(_('County name'), max_length=100)
    slug = models.SlugField()
    fips = models.CharField(_('County FIPS place code'), max_length=3)
    shape = models.MultiPolygonField(_('Region shape'), srid=4326, null=True)
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name=_('counties'),
    )

    class Meta:
        verbose_name_plural = _('counties')

    def __str__(self):
        return self.name

    @property
    def name_full(self):
        return '{0} County'.format(self.name)

    @property
    def name_cohorts(self):
        if self.name == 'El Paso':
            return 'El Paso and Hudspeth'
        else:
            return self.name

    @property
    def name_full_cohorts(self):
        if self.name == 'El Paso':
            return 'El Paso and Hudspeth County'
        else:
            return self.name_full

    @cached_property
    def shape_simple(self):
        return self.shape.simplify(0.01)


class CountyCohorts(CohortsBase):
    county = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        related_name='cohorts',
    )
    year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        related_name='county_cohorts',
    )

    class Meta:
        unique_together = (
            'county', 'year', 'economic_status', 'gender', 'ethnicity')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.county.name)
