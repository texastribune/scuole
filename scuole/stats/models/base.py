# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from .staff_student import StaffStudentBase
from .postsecondary_readiness import PostSecondaryReadinessBase


@python_2_unicode_compatible
class SchoolYear(models.Model):
    name = models.CharField(max_length=9)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


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
