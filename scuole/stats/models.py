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
    all_students_count = models.IntegerField('Number of students')
    asian_count = models.IntegerField('Number of Asian students')
    hispanic_count = models.IntegerField('Number of Hispanic students')
    pacific_islander_count = models.IntegerField(
        'Number of Pacific Islander students')
    white_count = models.IntegerField('Number of White students')

    class Meta:
        abstract = True
