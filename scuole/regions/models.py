# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.gis.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from scuole.cohorts.models import CohortsBase
from scuole.states.models import State
from scuole.stats.models import SchoolYear, StatsBase


class Region(models.Model):
    name = models.CharField(_('Geographic name for region'), max_length=20)
    region_id = models.CharField(_('Region identifier'), max_length=2)
    slug = models.SlugField()
    shape = models.MultiPolygonField(_('Region shape'), srid=4326, null=True)
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='regions',
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.region_id)

    @property
    def region_name(self):
        return 'Region {0}'.format(self.region_id)

    @property
    def region_name_with_city(self):
        return '{0} ({1})'.format(self.region_name, self.name)

    @cached_property
    def shape_simple(self):
        return self.shape.simplify(0.01)


class RegionStats(StatsBase):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='stats',
    )
    year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        related_name='region_stats',
    )

    class Meta:
        unique_together = ('region', 'year',)
        verbose_name_plural = _('Region stats')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.region.name)


class RegionCohorts(CohortsBase):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='cohorts',
    )
    year = models.ForeignKey(
        SchoolYear,
        on_delete=models.CASCADE,
        related_name='region_cohorts',
    )

    class Meta:
        unique_together = (
            'region', 'year', 'gender', 'ethnicity', 'economic_status',)
        verbose_name_plural = _('Region cohorts')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.region.name)
