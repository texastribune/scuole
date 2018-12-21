# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.gis.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from localflavor.us.models import USStateField

from scuole.cohorts.models import CohortsBase
from scuole.core.models import PersonnelBase
from scuole.core.utils import to_geojson_feature
from scuole.stats.models import SchoolYear, StatsBase


class State(models.Model):
    name = USStateField(_("State name"))
    slug = models.SlugField()
    shape = models.MultiPolygonField(_("State shape"), srid=4326, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("states:detail", kwargs={"slug": self.slug})

    @cached_property
    def shape_simple(self):
        return self.shape.simplify(0.01)

    @cached_property
    def as_geojson(self):
        return to_geojson_feature(self, "shape", ["name"])


class StateStats(StatsBase):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="stats")
    year = models.ForeignKey(
        SchoolYear, on_delete=models.CASCADE, related_name="state_stats"
    )

    class Meta:
        unique_together = ("state", "year")
        verbose_name_plural = _("State stats")

    def __str__(self):
        return "{0} {1}".format(self.year.name, self.state.name)


class Commissioner(PersonnelBase):
    state = models.OneToOneField(
        State, on_delete=models.CASCADE, related_name="commissioner_of"
    )

    def __str__(self):
        return "Texas Education Commissioner"


class StateCohorts(CohortsBase):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cohorts")
    year = models.ForeignKey(
        SchoolYear, on_delete=models.CASCADE, related_name="state_cohorts"
    )

    class Meta:
        unique_together = ("state", "year", "gender", "ethnicity", "economic_status")
        verbose_name_plural = _("State cohorts")

    def __str__(self):
        return "{0} {1}".format(self.year.name, self.state.name)
