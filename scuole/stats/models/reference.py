# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class ReferenceBase(models.Model):
    """
    An abstract model representing accountability ratings commonly tracked
    across all entities in TEA data. Meant to be used with StatsBase by other
    apps for establishing their stats models.

    """
    accountability_rating = models.CharField(
        'Accountability rating', null=True, blank=True, max_length=30)

    class Meta:
        abstract = True
