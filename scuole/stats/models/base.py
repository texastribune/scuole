# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models

from .postsecondary_readiness import PostSecondaryReadinessBase
from .staff_student import StaffStudentBase


class SchoolYear(models.Model):
    name = models.CharField(max_length=9)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    @property
    def ninth_grade_year(self):
        start, end = self.name.split("-")

        return "{}-{}".format(int(start) - 4, int(end) - 4)

    @property
    def previous_year(self):
        start_year = self.start_year - 1
        end_year = self.end_year - 1

        return f"{start_year}-{end_year}"

    @property
    def start_year(self):
        return int(self.name.split("-")[0])

    @property
    def end_year(self):
        return int(self.name.split("-")[1])


class StatsBase(StaffStudentBase, PostSecondaryReadinessBase):
    """
    An abstract model representing stats commonly tracked across all entities
    in TEA data. Meant to be the base used by other apps for establishing
    their stats models.

    Example:

    class CampusStats(StatsBase):
        ...

    """

    class Meta:
        abstract = True
