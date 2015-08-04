# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.stats.models import SchoolYear, StatsBase


@python_2_unicode_compatible
class State(models.Model):
    name = models.CharField(help_text="State name", max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class StateStats(StatsBase):
    state = models.ForeignKey(State, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='state_stats')

    class Meta:
        unique_together = ('state', 'year',)
        verbose_name_plural = 'State stats'

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.state.name)
