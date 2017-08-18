# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from localflavor.us.models import USStateField

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property

from scuole.core.models import PersonnelBase
from scuole.stats.models import SchoolYear, StatsBase
from scuole.cohorts.models import CohortsBase
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class State(models.Model):
    name = USStateField(_('State name'))
    slug = models.SlugField()
    shape = models.MultiPolygonField(_('State shape'), srid=4326, null=True)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('states:detail', kwargs={
            'slug': self.slug,
        })

    @cached_property
    def shape_simple(self):
        return self.shape.simplify(0.01)


@python_2_unicode_compatible
class StateStats(StatsBase):
    state = models.ForeignKey(State, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='state_stats')

    class Meta:
        unique_together = ('state', 'year',)
        verbose_name_plural = _('State stats')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.state.name)


@python_2_unicode_compatible
class Commissioner(PersonnelBase):
    state = models.OneToOneField(State, related_name='commissioner_of')

    def __str__(self):
        return 'Texas Education Commissioner'


@python_2_unicode_compatible
class StateCohorts(CohortsBase):
    state = models.ForeignKey(State, related_name='cohorts')
    year = models.ForeignKey(SchoolYear, related_name='state_cohorts')

    class Meta:
        unique_together = (
            'state', 'year', 'gender', 'ethnicity', 'economic_status',)
        verbose_name_plural = _('State cohorts')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.state.name)
