# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class SchoolYear(models.Model):
    name = models.CharField(max_length=9)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class StatsBase(models.Model):
    """
    An abstract model representing stats commonly tracked across all entities
    in TEA data. Meant to be the base used by other apps for establishing
    their stats models.

    Example:

    class CampusStats(StatsBase):
        ...

    """

    # Student counts
    all_students_count = models.IntegerField(
        'Number of students', null=True, blank=True)
    african_american_count = models.IntegerField(
        'Number of African American students', null=True, blank=True)
    asian_count = models.IntegerField(
        'Number of Asian students', null=True, blank=True)
    hispanic_count = models.IntegerField(
        'Number of Hispanic students', null=True, blank=True)
    pacific_islander_count = models.IntegerField(
        'Number of Pacific Islander students', null=True, blank=True)
    two_or_more_races_count = models.IntegerField(
        'Number of Two or More Races students', null=True, blank=True)
    white_count = models.IntegerField(
        'Number of White students', null=True, blank=True)

    # Student percents
    african_american_percent = models.FloatField(
        'Percent of African American students', null=True, blank=True)
    asian_percent = models.FloatField(
        'Percent of Asian students', null=True, blank=True)
    hispanic_percent = models.FloatField(
        'Percent of Hispanic students', null=True, blank=True)
    pacific_islander_percent = models.FloatField(
        'Percent of Pacific Islander students', null=True, blank=True)
    two_or_more_races_percent = models.FloatField(
        'Percent of Two or More Races students', null=True, blank=True)
    white_percent = models.FloatField(
        'Percent of White students', null=True, blank=True)

    class Meta:
        abstract = True
