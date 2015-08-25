# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from slugify import slugify

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.states.models import State
from scuole.stats.models import SchoolYear, StatsBase


@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField('Geographic name for region', max_length=20)
    region_id = models.CharField('Region identifier', max_length=2)
    slug = models.SlugField()
    state = models.ForeignKey(State, related_name='regions')

    def __str__(self):
        return '{} - {}'.format(self.name, self.region_id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Region, self).save(*args, **kwargs)


@python_2_unicode_compatible
class RegionStats(StatsBase):
    region = models.ForeignKey(Region, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='region_stats')

    class Meta:
        unique_together = ('region', 'year',)
        verbose_name_plural = 'Region stats'

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.region.name)
