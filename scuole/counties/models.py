# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.states.models import State
from scuole.cohorts.models import CohortsYear, CohortsBase
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class County(models.Model):
    name = models.CharField(_('County name'), max_length=100)
    slug = models.SlugField()
    fips = models.CharField(_('County FIPS place code'), max_length=3)
    state = models.ForeignKey(State, related_name=_('counties'))

    class Meta:
        verbose_name_plural = _('counties')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CountyCohorts(CohortsBase):
    county = models.ForeignKey(County, related_name='cohorts')
    year = models.ForeignKey(CohortsYear, related_name='county_cohorts')

    class Meta:
        unique_together = (
            'county', 'year', 'economic_status', 'gender')
        verbose_name_plural = _('County cohorts')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.county.name)
